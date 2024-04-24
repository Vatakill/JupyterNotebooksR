from testavimas_python_20240424 import sudetis, daugyba, rask_didziausia, hello

def test_sudetis():
    assert sudetis(1,2) == 3

def test_sudetis_neigiami():
    assert sudetis(-1,-5) == -6

def test_daugyba():
    assert daugyba(2, 5) == 10

def test_sudetis_2():
    num1, num2 = 5, 3
    res = 8
    faktinis_res = sudetis(num1, num2)
    assert res == faktinis_res, f'sudeties testas nepavyko: {num1} + {num2} turetu buti {res}, bet gavosi {faktinis_res}'

def test_rask_didziausia():
    num1, num2 = 10, 20
    res = 20
    f_res = rask_didziausia(num1, num2)
    assert f_res == res

def test_rask_didziausia_2():
    assert rask_didziausia(10,5) == 10
    assert rask_didziausia(5,10) == 10
    assert rask_didziausia(10, 10) == 10

def test_hello():
    assert hello('Tomas') == "Hello, Tomas"

import testavimas_python_20240424

def test_pirmas_sarase():
    skaiciai = [1,2,3,4,5]
    assert testavimas_python_20240424.pirmas_sarase(skaiciai) == 1

def test_pirmas_sarase_tuscias():
    skaiciai = []
    assert testavimas_python_20240424.pirmas_sarase(skaiciai) == None

def test_pirmas_sarase_tekstas():
    tekstas = 'labas'
    assert testavimas_python_20240424.pirmas_sarase(tekstas) == 'l'