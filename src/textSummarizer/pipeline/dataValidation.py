from textSummarizer.config.configuration import configurationManager
from textSummarizer.components.dataValidation import dataValidation
from textSummarizer.logging import logger

class dataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = configurationManager()
        data_validation_config = config.getDataValidationConfig()
        data_validation = dataValidation(config=data_validation_config)
        data_validation.validateAllFiles()