import configparser
import os
import logging

from data_factory.factory.helper import ObjectFactory
from .twitter_pubnub import TwitterPubnubHandler


def setup_logger(logger_name, log_message_level, log_message_format):
    """
    Setup LOGGER object to handle logging
    """

    logger = logging.getLogger(logger_name)
    stream_handler = logging.StreamHandler()
    logger.setLevel(log_message_level)
    formatter = logging.Formatter(log_message_format)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def setup_configuration():
    """
    Setup configuration by reading from the environment variable called DATA_FACTORY_CONFIGURATION.
    Default value is ../config/config.ini
    """

    configuration = configparser.ConfigParser()
    configuration.read(os.getenv('DATA_FACTORY_CONFIGURATION', '../../config/config.ini'))
    return configuration


"""
Setup object factory class
"""
factory = ObjectFactory()
configuration = setup_configuration()
logger = setup_logger(configuration['Logging']['LoggerName'],
                      configuration['Logging']['LogMessageLevel'],
                      '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
factory.register_handler('TwitterPubnub', TwitterPubnubHandler(configuration, logger))
