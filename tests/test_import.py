# -*- coding: utf-8 -*-

import pytest


def test():
    import my_package


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
