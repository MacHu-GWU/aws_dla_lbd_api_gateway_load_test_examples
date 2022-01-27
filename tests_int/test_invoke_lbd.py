# -*- coding: utf-8 -*-

import json
import boto3

boto_ses = boto3.session.Session()
lbd_client = boto_ses.client("lambda")
function_name = "my_load_test_app-dev-increment"
endpoint = "https://k2pae9du94.execute-api.us-east-1.amazonaws.com/api"

res = lbd_client.invoke(
    FunctionName=function_name,
    InvocationType="RequestResponse",
    Payload=json.dumps({"key": "test"}),
)
print(res["Payload"].read())
