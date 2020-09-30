import sys
import logging

from logger import Logger


class ExceptHookHandler:
    
    def __init__(self, logfile):
        self.__logfile = logfile
        self.__logger = Logger(level=logging.WARNING, handler=self.__logfile)

        sys.excepthook = self.__handle_exception
    
    def __handle_exception(self, exctype, excvalue, tb): 
        """exception handler

        :param exctype: exception type
        :param excvalue: exception value
        :param tb: trace back
        """
        try:
            self.__logger.error("ERROR：", exc_info=(exctype, excvalue, tb))
        except:
            pass
        
        sys.__excepthook__(exctype, excvalue, tb)     
        