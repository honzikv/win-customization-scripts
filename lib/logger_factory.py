import logging
import sys

def create_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Creates a logger object
    :param name: Name of the logger
    :param level: Level of the logger
    :return: Logger object
    """
    # Create the logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create the formatter
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s')
    
    # Create the console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(console_handler)
    
    return logger
