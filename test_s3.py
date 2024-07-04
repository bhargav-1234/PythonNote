import pytest
from moto import mock_aws
import os
import boto3
import json

from s3 import app, download_s3_file

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@mock_aws
def setup_s3(bucket_name, s3_key, content):
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket=bucket_name)
    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=content)

@mock_aws
def test_download_file_success_case(client):
    bucket_name = 'test-bucket'
    s3_key = 'test-file.txt'
    local_dir = '/tmp/download_file'
    setup_s3(bucket_name, s3_key, 'Hello, S3')
    res = client.post('/download', data=json.dumps({
        'bucket_name': bucket_name,
        's3_key': s3_key,
        'local_dir': local_dir
    }), content_type='application/json')

    assert res.status_code == 200
