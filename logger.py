import logging
import os

def setupLogger():
    logger = logging.getLogger("PhotoLogger")
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        logFilePath = os.path.join(scriptDir, "../logs/photoLog.txt")
        fileHandler = logging.FileHandler(logFilePath)
        fileHandler.setLevel(logging.DEBUG)


        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fileHandler.setFormatter(formatter)


        logger.addHandler(fileHandler)

    return logger

logger = setupLogger()
