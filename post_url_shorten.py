import json
from urllib.parse import urlsplit
from botocore.vendored import requests
import re
import boto3
import os
import string
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    slug = ''.join(random.choice(chars) for _ in range(size))
    return slug

def lambda_handler(event, context):
    body = json.loads(event['body'])
    long_url = body['url']
    if not re.match(r'http(s?)\:', long_url):
        long_url = 'http://' + long_url
    r = requests.get(long_url)
    formatted_url = r.url
    url_id = id_generator()
    response_url = os.environ['BASE_URL']+url_id
    result = table.put_item(
        Item={
            'url_id': url_id,
            'url': formatted_url
        }
    )
    resp = {
            "statusCode": 201,
            "body": response_url,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials" : "true",
                "Content-Type": "text/html; charset=utf-8"
            }
        }
    return resp
