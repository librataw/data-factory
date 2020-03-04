#!/usr/bin/env python
from data_factory.factory import source


config = {
    'channel_name': 'pubnub-twitter',
    'subscriber_key': 'sub-c-78806dd4-42a6-11e4-aed8-02ee2ddab7fe',
    'use_ssl': False
}

twitter_pubnub = source.factory.get_handler('TwitterPubnub', **config)
twitter_pubnub.fetch_data(limit=2)
