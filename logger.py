import logging

def setupLogger():
    logger = logging.getLogger("PhotoLogger")
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)


        fileHandler = logging.FileHandler("../logs/photoLog.txt")
        fileHandler.setLevel(logging.DEBUG)


        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fileHandler.setFormatter(formatter)


        logger.addHandler(fileHandler)

    return logger

logger = setupLogger()