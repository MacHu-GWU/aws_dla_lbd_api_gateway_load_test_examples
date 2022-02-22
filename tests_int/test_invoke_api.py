# -*- coding: utf-8 -*-

import pytest
import json
import requests
from my_package.lbd.increment import KeyValueCount

endpoint = "https://dpm3620drh.execute-api.us-east-1.amazonaws.com/api"

headers = {
    "Authorization": "allow",
    "Content-Type": "application/json",
}


def test():
    # ---------------------------------------------------------------
    # before state
    # ---------------------------------------------------------------
    key = "integration_test_invoke_api"
    item = KeyValueCount(key=key, count=0)
    item.save()

    # ---------------------------------------------------------------
    # invoke api
    # ---------------------------------------------------------------
    res = requests.post(
        f"{endpoint}/incr",
        headers=headers,
        data=json.dumps({"key": key}),
    )
    assert json.loads(res.text)["message"] == "success"
    assert res.status_code == 200

    # ---------------------------------------------------------------
    # after state
    # ---------------------------------------------------------------
    item.refresh()
    assert item.count == 1


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
