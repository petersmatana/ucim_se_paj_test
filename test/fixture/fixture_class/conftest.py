# -*- coding: utf-8 -*-


"""

    vubec netusim, pry bych mel mit class kterou
    zabalim testy, pak poustim tuhle tridu nad
    kterou se aplikuje fixture...
    kloudny priklad jsem nenasel

"""


import pytest


@pytest.fixture(scope='class', autouse=True)
def fixture_class():
    print 'class fixture'
