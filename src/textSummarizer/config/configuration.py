from textSummarizer.constants import configFilePath,paramsFilePath
from textSummarizer.utils.common import read_yaml,createDir
from textSummarizer.entity import *
class configurationManager:
    def __init__(
        self,
        config_FilePath = configFilePath,
        params_FilePath = paramsFilePath):
        
        self.config = read_yaml(config_FilePath)
        self.params = read_yaml(params_FilePath)
        
        createDir([self.config.artifacts_root])
    
    def getDataIngestionConfig(self) -> dataIngestionConfig:
        config = self.config.data_ingestion
        createDir([config.root_dir])
        
        data_ingestion_config = dataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def getDataValidationConfig(self)->dataValidationConfig:
        config = self.config.dataValidation
        createDir([config.rootDir])
        
        datavalidationconfig = dataValidationConfig(
            rootDir=config.rootDir,
            statusFile=config.statusFile,
            allRequiredFiles=config.allRequiredFiles
        )
        return datavalidationconfig

    def getDataTransformationConfig(self)->dataTransformationConfig:
        config = self.config.dataTransformation
        createDir([config.rootDir])
        
        datatransformationconfig = dataTransformationConfig(
            rootDir=config.rootDir,
            dataPath=config.dataPath,
            tokenizerName=config.tokenizerName
        )
        return datatransformationconfig
    
    def getModelTrainerConfig(self) -> modelTrainerConfig:
        config = self.config.modelTrainer
        params = self.params.trainingArguments
        
        createDir([config.rootDir])
        
        model_trainer_config = modelTrainerConfig(
            rootDir=config.rootDir,
            dataPath=config.dataPath,
            modelCkpt=config.modelCkpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            per_device_eval_batch_size=params.per_device_eval_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy= params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps,
            size= params.size,
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> modelEvaluationConfig:
        config = self.config.model_evaluation

        createDir([config.root_dir])

        model_evaluation_config = modelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )

        return model_evaluation_config