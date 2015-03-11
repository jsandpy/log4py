__author__ = 'JsAndPy'

import sys
import logging
import logging.handlers as handler
from rainbow_logging_handler import RainbowLoggingHandler

class Log4Py:
    def __init__(self):
        # Init logger debug
        self.__loggerDebug = self.__createLogger('debug', logging.DEBUG)
        self.__loggerError = self.__createLogger('error', logging.ERROR)
        self.__loggerInfo = self.__createLogger('info', logging.INFO)


    def __createLogger(self, logName, level):
        try:
            formatterConsole = logging.Formatter('%(asctime)s.%(msecs)d - %(message)s')
            formatterFile = logging.Formatter('%(asctime)s - %(message)s')

            logger = logging.getLogger(logName)
            logger.setLevel(level)

            # Log to console
            chColor = RainbowLoggingHandler(sys.stderr, datefmt='%Y-%m-%d %H:%M:%S')
            chColor.setFormatter(formatterConsole)
            chColor.setLevel(level)
            logger.addHandler(chColor)

            # Log to file
            path = 'logs/' + str(logName) + '.log'
            fh = handler.RotatingFileHandler(path, maxBytes=5*1024*1024, backupCount=1650)
            fh.setFormatter(formatterFile)
            fh.setLevel(level)
            logger.addHandler(fh)
            return logger
        except:
            print('Error create logger for python !')

    def debug(self, *args):
        message = 'DEBUG:'
        for x in args:
            message += ' ' + str(x)
        self.__loggerDebug.debug(message)

    def error(self, *args):
        message = 'ERROR:'
        for x in args:
            message += ' ' + str(x)
        self.__loggerError.error(message)

    def info(self, *args):
        message = 'INFO: '
        for x in args:
            message += ' ' + str(x)
        self.__loggerInfo.info(message)
