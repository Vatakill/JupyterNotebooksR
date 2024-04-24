from uzduotis1 import apverstas, ilgis, teigiami, rikiuoti, rikiuoti_mazejanciai, rikiuoti_didejant

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