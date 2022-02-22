# -*- coding: utf-8 -*-

import pytest
import json
import boto3
from my_package import __chalice_app_name__
from my_package.lbd.increment import KeyValueCount

boto_ses = boto3.session.Session()
lbd_client = boto_ses.client("lambda")
function_name = f"{__chalice_app_name__}-dev-increment"


def test_regular_case():
    # ---------------------------------------------------------------
    # before state
    # ---------------------------------------------------------------
    key = "integration_test_invoke_lbd_regular_case"
    item = KeyValueCount(key=key, count=0)
    item.save()

    # ---------------------------------------------------------------
    # invoke api
    # ---------------------------------------------------------------
    res = lbd_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps({"key": key}),
    )

    # ---------------------------------------------------------------
    # after state
    # ---------------------------------------------------------------
    assert json.loads(res["Payload"].read())["message"] == "success"
    item.refresh()
    assert item.count == 1

    # ---------------------------------------------------------------
    # invoke api again
    # ---------------------------------------------------------------
    res = lbd_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps({"key": key}),
    )

    # ---------------------------------------------------------------
    # after state
    # ---------------------------------------------------------------
    assert json.loads(res["Payload"].read())["message"] == "success"
    item.refresh()
    assert item.count == 2


def test_edge_case():
    """
    The key may not exists before.
    """
    # ---------------------------------------------------------------
    # before state
    # ---------------------------------------------------------------
    key = "integration_test_invoke_lbd_edge_case"
    item = KeyValueCount(key=key)
    if item.exists():
        item.delete()

    # ---------------------------------------------------------------
    # invoke api
    # ---------------------------------------------------------------
    res = lbd_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps({"key": key}),
    )

    # ---------------------------------------------------------------
    # after state
    # ---------------------------------------------------------------
    assert json.loads(res["Payload"].read())["message"] == "success"
    item.refresh()
    assert item.count == 1


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
