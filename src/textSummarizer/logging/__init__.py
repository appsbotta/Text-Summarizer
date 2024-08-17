import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
logFilePath = os.path.join(log_dir,"runningLogs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(logFilePath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TSLogger")