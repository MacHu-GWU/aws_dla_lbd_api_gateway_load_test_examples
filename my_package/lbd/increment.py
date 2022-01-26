# -*- coding: utf-8 -*-


from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import PAY_PER_REQUEST_BILLING_MODE


class KeyValueCount(Model):
    class Meta:
        table_name = "aws_dla_lbd_api_gateway_load_test_examples"
        region = "us-east-1"
        billing_mode = PAY_PER_REQUEST_BILLING_MODE

    key = UnicodeAttribute(hash_key=True)
    count = NumberAttribute(default=0)


KeyValueCount.create_table(wait=True)


def low_level_api(key: str):
    item = KeyValueCount(key=key)
    try:
        item.update(
            actions=[
                KeyValueCount.count.set(KeyValueCount.count + 1)
            ]
        )
    except:
        item.save()
    return {"message": "success"}


def handler(event, context):
    return low_level_api(event["key"])
