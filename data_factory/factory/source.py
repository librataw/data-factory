import json

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

from data_factory.factory.base import FactoryBase
from data_factory.factory.helper import ObjectFactory


class TwitterPubnub(FactoryBase):
    def __init__(self, channel_name, subscriber_key, use_ssl):
        self.channel_name = channel_name
        self.subscriber_key = subscriber_key
        self.use_ssl = use_ssl
        self.pubnub, self.listener = self.setup_connection()

    def setup_connection(self):
        _pnconfig = PNConfiguration()
        _pnconfig.subscribe_key = self.subscriber_key
        _pnconfig.ssl = self.use_ssl
        _pubnub = PubNub(_pnconfig)
        _listener = SubscribeListener()
        _pubnub.add_listener(_listener)
        _pubnub.subscribe().channels(self.channel_name).execute()
        _listener.wait_for_connect()
        return _pubnub, _listener

    def fetch_data(self, limit = 0):
        counter = 1
        while counter <= limit or limit == 0:
            result = json.dumps(self.listener.wait_for_message_on(self.channel_name).message)
            print(result)
            counter += 1

        self.pubnub.unsubscribe()


class TwitterPubnubHandler:
    def __init__(self):
        self._instance = None

    def __call__(self, channel_name, subscriber_key, use_ssl):
        if not self._instance:
            self.instance = TwitterPubnub(channel_name, subscriber_key, use_ssl)
        return self.instance


factory = ObjectFactory()
factory.register_handler('TwitterPubnub', TwitterPubnubHandler())
