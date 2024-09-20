import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk
from textSummarizer.entity import dataTransformationConfig

class dataTransformation:
    def __init__(self,config:dataTransformationConfig) -> None:
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizerName)
        
    def convertToFeatures(self,exampleBatch):
        inputEncoding = self.tokenizer(exampleBatch['dialogue'],max_length=1024,truncation=True,padding=True)
        
        with self.tokenizer.as_target_tokenizer():
            targetEncoding = self.tokenizer(exampleBatch['summary'],max_length=128,truncation=True,padding=True)
        return {
            'input_ids':inputEncoding['input_ids'],
            'attention_mask': inputEncoding['attention_mask'],
            'labels':targetEncoding['input_ids']
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.dataPath)
        dataset_samsum_pt = dataset_samsum.map(self.convertToFeatures,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.rootDir,'samsumDataset'))
        