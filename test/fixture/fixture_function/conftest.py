# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope='function')
def fixture_function():
    """Co jeden test, to se pusti takhle fixtura.
    """
    print 'fixture module, pousti se pro kazdy test zvlast'


@pytest.fixture(scope='module')
def fix_f():
    """Dobry je ze tady muzu dat dalsi fixturu...
    """
    print 'tady ale poustim fixture module'
