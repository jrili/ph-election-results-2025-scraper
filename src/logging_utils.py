import logging
from datetime import datetime

from . import config

logger = logging.getLogger(config.LOG_CONTEXT)

def init_logger(level=logging.DEBUG, console_level=logging.INFO):
    logger.setLevel(level)

    # Create file handler that will store log messages of `level` severity and higher
    file_handler = logging.FileHandler(config.PATH_TO_LOGFILE)
    file_handler.setLevel(level)

    # Create console handler that will also print `console_level` severity logs and higher
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)

    # Create formatter to add timestamps, log context name, and log severity level for each log
    formatter = logging.Formatter('%(asctime)s - %(name)s: %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add both the file and console handlers to the main logger object
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
