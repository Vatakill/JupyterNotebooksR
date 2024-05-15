from uzduotis1 import apverstas, ilgis, teigiami, rikiuoti, rikiuoti_mazejanciai, kartotinis3, raides, pirminis

def test_apverstas():
    txt = 'alus'
    assert apverstas(txt) == 'sula'
    txt = 'suo'
    assert apverstas(txt) == 'ous'
    # txt = 'suo'
    # assert apverstas(txt) == 'suo'

def test_ilgis():
    sarasas = [1,2,3]
    assert ilgis(sarasas) == 3
    sarasas = ['a', 'b', 'c', 'd']
    assert ilgis(sarasas) == 4
    # sarasas = ['a', 'b', 'c', 'd']
    # assert ilgis(sarasas) == 5

def test_teigiami():
    sarasas = [1, -2, 3, -4]
    assert teigiami(sarasas) == [1,3]
    # sarasas = [1, 2, 3, 4]
    # assert teigiami(sarasas) == [1,3]

# def test_rusiavimas():
#     sarasas = [1, -2, 3, -4]
#     assert rusiavimas('didejimo_tvarka', sarasas) == [-4,-2, 1, 3]
#     assert rusiavimas('mazejimo_tvarka', sarasas) == [3,1,-2,-4]


def test_rikiuoti_mazejanciai():
    assert rikiuoti(rikiuoti_mazejanciai, [1, -2, 3, -4]) == [3,1,-2,-4]

import pytest

@pytest.mark.parametrize('sk, ats', 
                         [(1, False), 
                         (3, True), 
                         (6, True)])
def test_kartotinis3(sk, ats):
    assert kartotinis3(sk) == ats


@pytest.mark.parametrize('zodziu_sarasas, atrinkti_zodziai',
[(['lape', 'kiaune', 'krokodilas'], ['krokodilas']),
 (['antanas', 'jonas', 'vytautas'], ['antanas', 'vytautas']),
 (['medis', 'zole', 'krumas'], [])])
def test_raides(zodziu_sarasas, atrinkti_zodziai):
    assert raides(zodziu_sarasas) == atrinkti_zodziai


@pytest.mark.parametrize('skaicius, ats', [
    (2, True),
    (3, True),
    (6, False),
    (47, True),
    (103, True)])

def test_pirminis(skaicius, ats):
    assert pirminis(skaicius) == ats