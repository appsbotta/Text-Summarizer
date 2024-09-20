from textSummarizer.config.configuration import configurationManager
from textSummarizer.components.dataTransformation import dataTransformation
from textSummarizer.logging import logger

class dataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = configurationManager()
        data_transformation_config = config.getDataTransformationConfig()
        data_transformation = dataTransformation(config=data_transformation_config)
        data_transformation.convert()