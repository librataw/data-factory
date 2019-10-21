#!./venv/bin/python

import boto3
import time

client = boto3.client('kinesis')

response = client.describe_stream(StreamName='twitter-stream')
print(response)
print(response['StreamDescription']['Shards'][0])
print(response['StreamDescription']['Shards'][1])
print(response['StreamDescription']['Shards'][2])
'''
shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = client.get_shard_iterator(StreamName='twitter-stream', ShardId=shard_id, ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']

record_response=client.get_records(ShardIterator=my_shard_iterator, Limit=2)


while('NextShardIterator' in record_response):
    record_response=client.get_records(ShardIterator=record_response['NextShardIterator'], Limit=2)
    print(record_response)
    time.sleep(2)
'''
