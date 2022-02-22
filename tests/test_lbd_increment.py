# -*- coding: utf-8 -*-

import pytest
from my_package.lbd.increment import low_level_api, KeyValueCount


def test_low_level_api():
    # ---------------------------------------------------------------
    # before state
    # ---------------------------------------------------------------
    # if the lambda function is stateful, put some code here
    # to simulate the state before lambda invoke
    # for example, if your lambda will copy a s3 object from
    # one place to another, you can create the source object here
    # ---------------------------------------------------------------
    key = "unit_test"
    item = KeyValueCount(key=key, count=0)
    item.save()

    # ---------------------------------------------------------------
    # invoke api
    # ---------------------------------------------------------------
    response = low_level_api(key=key)
    assert response["message"] == "success"

    # ---------------------------------------------------------------
    # after state
    # ---------------------------------------------------------------
    # if the lambda function is stateful, put some code here
    # to validate the state after lambda invoke
    # for example, if your lambda will copy a s3 object from
    # one place to another, you can validate if the destination
    # object is copied.
    # ---------------------------------------------------------------
    item = KeyValueCount.get(key)
    assert item.count == 1


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
