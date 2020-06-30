import boto3
import uuid

db = boto3.client('dynamodb')


def save_search_response(response):
    response['transaction_id'] = uuid.uuid4()
    db.Table('searches').put_item(response)
