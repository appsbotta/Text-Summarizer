from textSummarizer.config.configuration import configurationManager
from textSummarizer.components.dataIngestion import dataIngestion
from textSummarizer.logging import logger

class dataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = configurationManager()
        data_ingestion_config = config.getDataIngestionConfig()
        data_ingestion = dataIngestion(config=data_ingestion_config)
        data_ingestion.downloadFiles()
        data_ingestion.extractZip()