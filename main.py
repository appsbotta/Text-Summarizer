from textSummarizer.pipeline import dataTransformation
from textSummarizer.pipeline.dataIngestion import dataIngestionTrainingPipeline
from textSummarizer.pipeline.dataValidation import dataValidationTrainingPipeline
from textSummarizer.pipeline.dataTransformation import dataTransformationTrainingPipeline
from textSummarizer.pipeline.modelTrainer import modelTrainerTrainingPipeline
from textSummarizer.pipeline.modelEvaluation import modelEvaluationTrainingPipeline
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

stageName = "Model Trainer stage"
 
try:
    logger.info(f">>>>>>> stage {stageName} started <<<<<<<") 
    modelTrainer = modelTrainerTrainingPipeline()
    modelTrainer.main()
    logger.info(f">>>>>>> stage {stageName} completed <<<<<<\n\nx===========x\n")
except Exception as e:
    logger.exception(e)
    raise e

stageName = "Model Evaluation stage"
 
try:
    logger.info(f">>>>>>> stage {stageName} started <<<<<<<") 
    modelTrainer = modelEvaluationTrainingPipeline()
    modelTrainer.main()
    logger.info(f">>>>>>> stage {stageName} completed <<<<<<\n\nx===========x\n")
except Exception as e:
    logger.exception(e)
    raise e