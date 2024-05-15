# 1 užduotis
# Parašykite funkciją, kuri kaip argumentą priima vieną kintamąjį (tekstą) ir grąžina jį apversta
# pavyzdžiui, pateikus žodį "labas", funkcija grąžintų atsakymą "sabal"
# pateikus žodį "alus", grąžintų "sula"
# parašykite keletą testų šiai funkcijai
def apverstas(zodis):
    return zodis[::-1]

# 2 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina to sąrašo narių sumą
# parašykite keletą testų šiai funkcijai
def ilgis(sarasas):
    return len(sarasas)

# 3 užduotis
# parašykite funkciją, kuri kaip argumentą priima sąrašą ir grąžina jame esančius TEIGIAMUS skaičius
# parašykite keletą testų šiai funkcijai
def teigiami(sarasas):
    teigiami_sk = []
    for sk in sarasas:
        if sk > 0:
            teigiami_sk.append(sk)
    return teigiami_sk

# 4 užduotis
# Parašykite funkciją, kuri priima dvi sąrašų rūšiavimo funkcijas: vieną didėjančiai rūšiavimui, kitą mažėjančiai rūšiavimui, ir sąrašą skaičių. 
# Funkcija turi grąžinti rūšiuotą sąrašą pagal pateiktas rūšiavimo funkcijas.
# parašykite keletą testų šiai funkcijai
def rikiuoti(rikiavimo_funkcija, sarasas):
    return rikiavimo_funkcija(sarasas)

def rikiuoti_mazejanciai(sarasas):
    return sorted(sarasas, reverse=True)

def rikiuoti_didejant(sarasas):
    return sorted(sarasas)

# print(rikiuoti(rikiuoti_mazejanciai, [5,3,4,1,6,9]))


# 1 Užduotis
# Sukurkite funkciją, kuri patikrintų ar skaičius dalinasi iš 3
# Parašykite keletą testų (naudojantis parametrize)
def kartotinis3(sk):
    return sk % 3 == 0

# 2 užduotis 
# Parašykite funkciją rasti_pasikartojancias_raides, kuri priima sąrašą žodžių ir grąžina sąrašą tų žodžių
# kurie turi bent vieną pasikartojančią raidę.
# Parašykite keletą testų (naudojantis parametrize)
def raides(zodziu_sarasas):
    atrinkti_zodziai = []
    for zodis in zodziu_sarasas:
        if len(set(zodis)) < len(zodis):
            atrinkti_zodziai.append(zodis)
    return atrinkti_zodziai

# [i for i in x if len(i) > len(set(i))]

# 3 užduotis 
# Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis. 
# Grąžinkite True, jei skaičius yra pirminis, ir False, jei ne.
# Parašykite keletą testų (naudojantis parametrize)
def pirminis(sk):
    if sk <= 1:
        return False
    for e in range(2, sk):
        if sk % e == 0:
            return False
    else:
        return True

     

