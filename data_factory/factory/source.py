from data_factory.factory.base import FactoryBase


class TwitterPubnub(FactoryBase):
    def __init__(self, channel_name, subscriber_key, use_ssl):
        self.channel_name = channel_name
        self.subscriber_key = subscriber_key
        self.use_ssl = use_ssl

    def fetch_data(self):
        pass

class TwitterPubnubBuilder:
    def __init__(self):
        self._instance = None