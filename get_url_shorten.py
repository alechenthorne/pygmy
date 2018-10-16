import os
import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    if event['path'] is '/':
        return {
            "statusCode": 301, 
            "headers": {
                "Location": os.environ['ROOT_URL']
            }
        }
    url_id = json.dumps(event['pathParameters']['url_id'])
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    print("Table "+os.environ['DYNAMODB_TABLE']+" url_id "+url_id)
    result = table.get_item(
        Key={
            'url_id': json.loads(url_id)
        }
    )
    
    if 'Item' in json.dumps(result):
        url = json.dumps(result['Item']['url'])
        
        resp = {
            "statusCode": 301,
            "headers": {
                "Location": json.loads(url)
            }
        }
    else:
        resp = {
            "statusCode": 404,
            "body": "Not found.",
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials" : "true",
                "Content-Type": "application/json"
            }
        }
    return resp
