"""
Create a LoggingSystem to structure stdout content

TODO:
    - add different levels logging
    - add table support
"""

import logging
import os
import errno


def silentremove(filepath: str) -> None:
    """To remove a file that may not exit

    :param filepath: the file location
    :type filepath: str
    """
    try:
        os.remove(filepath)
    except OSError as e:
        # if the error is not FILE NOT FOUND
        if e.errno != errno.ENOENT:
            raise


class Logger:
    
    def __init__(
        self, 
        level: int = logging.DEBUG,
        handler: str = 'logfile.log',
        mode: str = 'a'
    ):
        # create a logger
        self.log = logging.getLogger(__name__)
        
        # set loggin level
        assert level in [0, 10, 20, 30, 40, 50], \
            "c.f. https://docs.python.org/3/library/logging.html#levels" 
        self.log.setLevel(level)
        
        # check file writing mode
        assert mode in 'wa'
        if mode == 'w':
            silentremove(handler)
        
        # define file handler and set formatter
        handler = logging.FileHandler(handler)
        formatter = logging.Formatter(self.__format)
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
    
    @property
    def __format(self):
        return '%(asctime)s : %(levelname)8s : %(name)s : %(message)s'

    def debug(self, msg: str) -> None:
        self.log.debug(msg)
    
    def info(self, msg: str) -> None:
        self.log.info(msg)
        
    def warning(self, msg: str) -> None:
        self.log.warning(msg)
        
    def error(self, msg: str) -> None:
        self.log.error(msg)
        
    def critical(self, msg: str) -> None:
        self.log.critical(msg)


if __name__ == "__main__":
    # Logs
    logger = Logger(mode='w')
    logger.debug('A debug message')
    logger.info('An info message')
    logger.warning('Something is not right.')
    logger.error('A Major error has happened.')
    logger.critical('Fatal error. Cannot continue')