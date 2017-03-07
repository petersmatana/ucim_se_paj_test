
"""

    FANTAZIE!!
    zil jsem v domeni, ze fixtury musi byt nasazene v souboru
    conftest? nevim ale proste jsem si do teto chvile myslel
    ze tomu tak musi byt

"""


from soubor_s_fixturama import fix1, fix2, fix3, fix4


def test_hodnefix_jedna(fix1, fix2):
    print 'test jedna'


def test_hodnefix_dva(fix1, fix3, fix4):
    print 'test dva'
