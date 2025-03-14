from textSummarizer.config.configuration import configurationManager
from textSummarizer.components.model_trainer import modelTrainer
from textSummarizer.logging import logger

class modelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = configurationManager()
        model_trainer_config = config.getModelTrainerConfig()
        model_trainer_config = modelTrainer(config=model_trainer_config)
        model_trainer_config.train()