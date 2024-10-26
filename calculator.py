import os

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(level=getattr(logging, log_level, logging.INFO), 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Calculator started")

