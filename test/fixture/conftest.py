# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="session", autouse=False)
def fixture_session():
    """Session scope chapu jako globalni test.

    Zajimavy je argument autouse=True, ktery test spusti
    anizbych ho pridaval jako argument k testum
    """
    print 'session fixture'
