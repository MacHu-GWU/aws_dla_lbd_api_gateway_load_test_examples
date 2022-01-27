# -*- coding: utf-8 -*-

import json
import requests

endpoint = "https://k2pae9du94.execute-api.us-east-1.amazonaws.com/api"

headers = {
    "Authorization": "allow",
    "Content-Type": "application/json",
}

res = requests.post(
    f"{endpoint}/incr",
    headers=headers,
    data=json.dumps({"key": "test"}),
)

print(res.text)
print(res.status_code)
