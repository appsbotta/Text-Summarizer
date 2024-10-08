from textSummarizer.pipeline import dataTransformation
from textSummarizer.pipeline.dataIngestion import dataIngestionTrainingPipeline
from textSummarizer.pipeline.dataValidation import dataValidationTrainingPipeline
from textSummarizer.pipeline.dataTransformation import dataTransformationTrainingPipeline
from textSummarizer.logging import logger

stageName = "Data Ingestion stage"
 
try:
    logger.info(f">>>>>>> stage {stageName} started <<<<<<<") 
    dataIngestion = dataIngestionTrainingPipeline()
    dataIngestion.main()
    logger.info(f">>>>>>> stage {stageName} completed <<<<<<\n\nx===========x\n")
except Exception as e:
    logger.exception(e)
    raise e


stageName = "Data Validation stage"
 
try:
    logger.info(f">>>>>>> stage {stageName} started <<<<<<<") 
    dataValidation = dataValidationTrainingPipeline()
    dataValidation.main()
    logger.info(f">>>>>>> stage {stageName} completed <<<<<<\n\nx===========x\n")
except Exception as e:
    logger.exception(e)
    raise e

stageName = "Data Transformation stage"
 
try:
    logger.info(f">>>>>>> stage {stageName} started <<<<<<<") 
    dataTransformation = dataTransformationTrainingPipeline()
    dataTransformation.main()
    logger.info(f">>>>>>> stage {stageName} completed <<<<<<\n\nx===========x\n")
except Exception as e:
    logger.exception(e)
    raise e