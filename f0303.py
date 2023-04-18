nevek:list[str] = []
nev:str = '---'
while nev != '':
    nev = input('írj be egy nevet: ')
    if nev != '': nevek.append(nev)
nevek.sort()
print(nevek)