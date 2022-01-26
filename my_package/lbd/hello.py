# -*- coding: utf-8 -*-

def low_level_api(name):
    message = f"hello {name}"
    return {"message": message}


def handler(event, context):
    return low_level_api(event.get("name", "Mr X"))
