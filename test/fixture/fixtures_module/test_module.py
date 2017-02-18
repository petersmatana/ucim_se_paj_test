# -*- coding: utf-8 -*-

from src.begin import scitani


def test_1(fixture_session):
    assert 4 == scitani(2, 2)
    print 'test_1'


def test_2(fixture_session):
    assert 0 == scitani(1, -1)
    print 'test_2'
