import os
from textSummarizer.logging import logger
from textSummarizer.entity import dataValidationConfig

class dataValidation:
    def __init__(self,config:dataValidationConfig) -> None:
        self.config = config
    
    def validateAllFiles(self)->bool:
        try:
            validateStatus = bool(None)
            all_files = os.listdir(os.path.join("artifacts",'data_ingestion','samsum_dataset'))
            
            for file in all_files:
                if file not in self.config.allRequiredFiles:
                    validateStatus = False
                    with open(self.config.statusFile,'w') as f:
                        f.write(f"validation status : {validateStatus}")
                else:
                    validateStatus = True
                    with open(self.config.statusFile,'w') as f:
                        f.write(f"validation status : {validateStatus}")
            return validateStatus
        except Exception as e:
            raise e