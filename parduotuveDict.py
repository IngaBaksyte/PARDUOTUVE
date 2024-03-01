# Byloje parduotuve.txt yra surašyti prekių pavadinimai ir kaina (naudojamas dict tipas).
# Byloje sarasas.txt yra surašyti prekių pavadinimai ir perkami kiekiai. Byloje sarasas.txt 
# prekių pavadinimų gali būti ir tokių, kokių nėra byloje parduotuve.txt. Parašykite 
# programą, kuri sukurtu bylą cekis.txt, kurioje būtų pateikta apsipirkimo informacija, 
#  ir bylą neradom.txt, kurioje pateikta informacija kokių prekių neradome ir reikalingi
#   jų kiekiai (kiekiai paimami iš sarasas.txt) 

# cekis.txt pav.
# Traškučiai OHO!         0.69 X 1        0.69 
# Traškučiai ESTRELLA     3.39 X 2        6.78 
# Gėrimas COCA-COLA, 1l   1.37 X 10      13.70
# Kūčiukai BEATOS         1.45 X 2        2.90 
# Persimonai              3.99 X 1,248    4.98 
# =============================================
# Mokėti 					             29.05  

def valytiByla(byla):
    with open(byla, 'w') as f:
        pass

def rasytiIByla(byla, txt):
    with open(byla, 'a', encoding='utf-8') as f:
        f.write(txt + '\n')

def skaitomByla(byla):
    with open(byla, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def pirkti():
    for preke in sarasas.keys():
        if preke in parduotuve.keys():
            suma = sarasas[preke] * parduotuve[preke]
            rasytiIByla('10cekis.txt', f"{preke:30} {str(parduotuve[preke]) + ' X ' + str(sarasas[preke]):15} {suma:5.2f}")
        else:
            rasytiIByla('10neradom.txt', f"{preke:20} {sarasas[preke]:4}")

import json

valytiByla('cekis.txt')
valytiByla('neradom.txt')
sarasas = skaitomByla('sarasas.json')
parduotuve = skaitomByla('parduotuve.json')

pirkti()