#!./venv/bin/python

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

import boto3
import time
import json

channel_name = 'pubnub-twitter'

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-78806dd4-42a6-11e4-aed8-02ee2ddab7fe'
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
pubnub.subscribe().channels(channel_name).execute()
my_listener.wait_for_connect()
print('connected')

client = boto3.client('kinesis')

counter = 0
while(True):
    Data = json.dumps(my_listener.wait_for_message_on(channel_name).message)
    print('Data to be loaded: %s' % Data)
    response = client.put_record(StreamName='twitter-stream', Data=Data, PartitionKey='1')
    print('Response: %s' % response)
    time.sleep(1)
    counter += 1

pubnub.unsubscribe()
print('unsubscribed')


