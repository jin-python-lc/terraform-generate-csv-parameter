import json
import boto3
import pandas as pd

json_open = open('state.json', 'r')
json_load = json.load(json_open)

json = json_load['values']['root_module']['resources']

df = pd.json_normalize(json)

df.to_csv('./state.csv')

s3 = boto3.resource('s3')
s3.Bucket('s3_bucket_name').upload_file(Filename='state.csv', Key='state.csv')
