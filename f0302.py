from random import randint

szamok:list[int] = []

for x in range(20):
    vlsz:int = randint(50, 150)
    szamok.append(vlsz)

szamok.sort()
print(szamok)

osszeg:int = sum(szamok)
elemszam:int = len(szamok)
atlag = osszeg / elemszam
print(f'számok összege: {osszeg}')
print(f'számok átlaga: {atlag}')

# megszámlálás tétele [ez egy programozási tétel]

# számláló:egész = 0
# ciklus, ami végigmegy minden elemen
#   feltétel, ami vizsgálja,
#   hogy az adott kritériumnak megfelel-e a lista eleme
#       # ha igaz, akkor: a számlálót megnövelem egyel

szamlalo:int = 0
for szam in szamok:
    if szam % 10 == 0:
        szamlalo += 1
print(f'0-ra végződő elemek száma: {szamlalo}')
