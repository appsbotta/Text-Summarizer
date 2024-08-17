import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import getFileSize
from textSummarizer.entity import dataIngestionConfig
from pathlib import Path

class dataIngestion:
    def __init__(self,config:dataIngestionConfig):
        self.config = config
    def downloadFiles(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"file already exists of size : {getFileSize(Path(self.config.local_data_file))}")
    
    def extractZip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)