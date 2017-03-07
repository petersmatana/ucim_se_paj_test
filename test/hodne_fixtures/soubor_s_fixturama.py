import pytest


@pytest.fixture
def fix1():
    print 'fixture 1'


@pytest.fixture
def fix2():
    print 'fixture 2'


@pytest.fixture
def fix3():
    print 'fixture 3'


@pytest.fixture
def fix4():
    print 'fixture 4'
