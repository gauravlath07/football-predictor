import sys, os
import logging
from logging.handlers import TimedRotatingFileHandler

class Logger:
    # class member constants
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    NONE = logging.NOTSET

    def __init__(self, fileName, level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s"):
        # add log directory if it doesn't already exist
        path = '{0}/logs'.format(os.getcwd())
        if not os.path.exists(path):
            os.makedirs(path)

        # make sure file eists    
        open('logs/'+fileName, 'a').close()
        
        # set the appropriate settings for the logger
        self.logger = logging.getLogger(fileName)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(format)
        
        self.file_handler = TimedRotatingFileHandler("logs/" + fileName,
                                       when='D',
                                       interval=1,
                                       backupCount=30)
        self.file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        # add the file and console logging handlers to the logger
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(console_handler)

    def changeLevel(self, level):
        self.logger.setLevel(level)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
    
    def warn(self, message):
        self.logger.warning(message)