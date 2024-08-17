from textSummarizer.constants import configFilePath,paramsFilePath
from textSummarizer.utils.common import read_yaml,createDir
from textSummarizer.entity import dataIngestionConfig

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