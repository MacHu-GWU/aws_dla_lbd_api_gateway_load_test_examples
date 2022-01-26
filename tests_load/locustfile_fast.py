# -*- coding: utf-8 -*-


import json
from locust import task, FastHttpUser, constant

# make sure it ends with /
api_gateway_endpoint = "https://tu562r0v73.execute-api.us-east-1.amazonaws.com/api/"

# HTTP header for authentication and other purpose
headers = {
    "Authorization": "allow",
    "Content-Type": "application/json",
}


# A coroutine, non blocker, async, high concurrent HTTP client
class FastUser(FastHttpUser):
    # since you defined the host, you can use relative path in your task
    host = api_gateway_endpoint

    # add 1 sec delay for all user. once one task is fired, it wait 1 sec to
    # fire another one
    wait_time = constant(1)

    @task
    def call_api(self):
        response = self.client.post(
            "incr",
            headers=headers,
            data=json.dumps({"key": "test"}),
        )
        print(response.text)
