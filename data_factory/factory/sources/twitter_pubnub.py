import json
import logging

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

from data_factory.factory.base import FactoryBase


class TwitterPubnub(FactoryBase):
    """
    TwitterPubnub class
    """

    def __init__(self, channel_name, subscriber_key, use_ssl=False, logger=None):
        """
        TwitterPubnub initiator
        :param channel_name: the twitter channel name from https://www.pubnub.com/developers/realtime-data-streams/twitter-stream/
        :param subscriber_key: subscriber key from https://www.pubnub.com/developers/realtime-data-streams/twitter-stream/
        :param use_ssl: use ssl option
        :param logger: logging object for logging purposes
        """
        self.channel_name = channel_name
        self.subscriber_key = subscriber_key
        self.use_ssl = use_ssl
        self.logger = logger or logging.getLogger(__name__)
        self.listener = self.setup_connection()

    def setup_connection(self):
        """
        The setup of connection to pubnub to ingest data
        :return:
        """
        try:
            self.logger.debug('Setup twitter pubnub connection')
            pnconfig = PNConfiguration()
            pnconfig.subscribe_key = self.subscriber_key
            pnconfig.ssl = self.use_ssl
            pubnub = PubNub(pnconfig)
            listener = SubscribeListener()
            pubnub.add_listener(listener)
            pubnub.subscribe().channels(self.channel_name).execute()
            listener.wait_for_connect()
            self.logger.debug('Finish setting up twitter pubnub connection')
            return listener
        except:
            self.logger.exception(Exception)

    def fetch_data(self):
        """
        Fetch streaming data from pubnub.
        Since this is a streaming data, everytime this function is called, it will return the latest data from Twittter.
        :return:
        """
        return json.dumps(self.listener.wait_for_message_on(self.channel_name).message)

    def __str__(self):
        """
        The str object for class print purposes
        :return:
        """
        self.logger.info('TwitterPubnub')


class TwitterPubnubHandler:
    """
    TwitterPubnubHandler class
    Handler class to initiate the TwitterPubnub class
    """

    def __init__(self, configuration, logger = None):
        """
        TwitterPubnubHandler initiator
        :param configuration: the configuration file object that's passed on from the sources __init__.py
        :param logger: logging object
        """
        self.instance = None
        self.configuration = configuration
        self.logger = logger or logging.getLogger(__name__)

    def __call__(self):
        """
        TwitterPubnubHandler call
        :return:
        """
        if not self.instance:
            self.logger.debug('Initialising TwitterPubnub class')
            self.instance = TwitterPubnub(self.configuration['TwitterPubnub']['ChannelName'],
                                          self.configuration['TwitterPubnub']['SubscriberKey'],
                                          self.configuration['TwitterPubnub']['UseSSL'],
                                          self.logger)
            self.logger.debug('Finish initialising TwitterPubnub class')
        return self.instance

    def __str__(self):
        """
        TwitterPubnubHandler str function
        :return:
        """
        self.logger.info('TwitterPubnubHandler')
