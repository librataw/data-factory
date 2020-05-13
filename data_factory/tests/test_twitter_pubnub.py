#!/usr/bin/env python

from data_factory.factory import sources

handlers = sources.factory.get_handlers()

twitter_pubnub = sources.factory.get_handler('TwitterPubnub')
print(twitter_pubnub.fetch_data())
