from transformers import TrainingArguments,Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from datasets import load_dataset,load_from_disk
from textSummarizer.entity import modelTrainerConfig
import torch
import os
from datasets import Dataset

class modelTrainer:
    def __init__(self,config:modelTrainerConfig):
        self.config = config



    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.modelCkpt)
        modelPagasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.modelCkpt).to(device)
        seq2seqDataCollator = DataCollatorForSeq2Seq(tokenizer,modelPagasus)
        
        dataset_samsum_pt = load_from_disk(self.config.dataPath)

        dataset_split = dataset_samsum_pt["train"]
        random_reduced_dataset = dataset_split.shuffle(seed=42).select(range(self.config.size))

        val_data = dataset_samsum_pt["validation"]

        trainer_args = TrainingArguments(
            output_dir = str(self.config.rootDir), 
            num_train_epochs=self.config.num_train_epochs, 
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, 
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay, 
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.evaluation_strategy, 
            eval_steps=self.config.eval_steps, save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        ) 

        trainer = Trainer(
            model=modelPagasus, 
            args=trainer_args,
            processing_class=tokenizer, 
            data_collator=seq2seqDataCollator,
            train_dataset= random_reduced_dataset,#dataset_samsum_pt["train"],
            eval_dataset= val_data,
        )
        
        trainer.train()

        ## Save model
        modelPagasus.save_pretrained(os.path.join(self.config.rootDir,"pegasus-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.rootDir,"tokenizer"))