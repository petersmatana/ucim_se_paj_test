# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="module", autouse=False)
def fixture_module():
    """Fixtura, co se pusti po vsechny testy jen jednou.
    Ale v ramci tohoto adresare. Pokud bych to dal do argumentu
    testu v fixture_function.test_function.test_3 tak to spadne.

    autouse se chova podobne jako u session fixture. pokud je
    True, pusti se nad celym adresarem
    """
    print 'fixture module, pousti se pro cely modul'
