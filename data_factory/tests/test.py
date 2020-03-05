#!/usr/bin/env python
from data_factory.factory import sources


config = {
    'channel_name': 'pubnub-twitter',
    'subscriber_key': 'sub-c-78806dd4-42a6-11e4-aed8-02ee2ddab7fe',
    'use_ssl': False
}

handlers = sources.factory.get_handlers()
import pdb;pdb.set_trace()

twitter_pubnub = sources.factory.get_handler('TwitterPubnub', **config)
twitter_pubnub.fetch_data(limit=2)
