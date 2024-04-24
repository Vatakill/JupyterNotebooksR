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



