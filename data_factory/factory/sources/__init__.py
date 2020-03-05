from data_factory.factory.helper import ObjectFactory
from .twitter_pubnub import TwitterPubnubHandler


factory = ObjectFactory()
factory.register_handler('TwitterPubnub', TwitterPubnubHandler())
