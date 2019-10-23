#!./venv/bin/python

import boto3
import time
import datetime

client = boto3.client('kinesis')

response = client.describe_stream(StreamName='twitter-stream')
print(response)
print(response['StreamDescription']['Shards'][0])
print(response['StreamDescription']['Shards'][1])
print(response['StreamDescription']['Shards'][2])

shard_id = response['StreamDescription']['Shards'][0]['ShardId']

the_time = datetime.datetime.now()

shard_iterator = client.get_shard_iterator(StreamName='twitter-stream', ShardId=shard_id,
                                           ShardIteratorType='AFTER_SEQUENCE_NUMBER',
                                           StartingSequenceNumber='49600701908632681759848763337425631711829410102084894722')['ShardIterator']



while(True):
    record_response = client.get_records(ShardIterator=shard_iterator, Limit=1)
    shard_iterator = record_response['NextShardIterator']
    print(record_response)
    time.sleep(1)

