from textSummarizer.pipeline.dataIngestion import dataIngestionTrainingPipeline
from textSummarizer.logging import logger

stageName = "Data Ingestion stage"
 
try:
    logger.info(f">>>>>>> stage {stageName} started <<<<<<<") 
    dataIngestion = dataIngestionTrainingPipeline()
    dataIngestion.main()
    logger.info(f">>>>>>> stage {stageName} completed <<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e