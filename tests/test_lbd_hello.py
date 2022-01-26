# -*- coding: utf-8 -*-

import pytest
from my_package.lbd.hello import low_level_api

def test_low_level_api():
    #---------------------------------------------------------------
    # before state
    #---------------------------------------------------------------
    # if the lambda function is stateful, put some code here
    # to simulate the state before lambda invoke
    # for example, if your lambda will copy a s3 object from
    # one place to another, you can create the source object here



    #---------------------------------------------------------------
    # invoke api
    #---------------------------------------------------------------
    response = low_level_api(name="alice")
    # validate response
    assert response["message"] == "hello alice"

    #---------------------------------------------------------------
    # after state
    #---------------------------------------------------------------
    # if the lambda function is stateful, put some code here
    # to validate the state after lambda invoke
    # for example, if your lambda will copy a s3 object from
    # one place to another, you can validate if the destination
    # object is copied.
    
    
    
    #---------------------------------------------------------------
    


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
