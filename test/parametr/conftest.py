# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='function', params=[1, 2, 3])
def parametry(request):
    print request.param
