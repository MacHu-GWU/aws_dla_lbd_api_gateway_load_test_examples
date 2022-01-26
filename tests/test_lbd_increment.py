# -*- coding: utf-8 -*-

import pytest
from my_package.lbd.increment import low_level_api, KeyValueCount


def test_low_level_api():
    key = "test"
    item = KeyValueCount(key=key, count=0)
    item.save()

    response = low_level_api(key=key)
    assert response["message"] == "success"

    item = KeyValueCount.get(key)
    assert item.count == 1


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
