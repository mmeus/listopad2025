dane = [w.strip() for w in open('hasla.txt')]

#zad3.1
licznik = 0
for h in dane:
    if len(h) >= 12:
        if '$' in h or '!' in h or '%' in h:
            licznik += 1
#print(licznik)

#zad3.2
def czy_pierwsza(liczba):
    licznik = 0
    for x in range(1, liczba + 1): #można zrobić do pół liczby, albo nawet pierwiastka z niej
        if liczba % x == 0:
            licznik += 1
    return licznik == 2

#Metoda chałupnicza
'''for h in dane:
    czy_ok = True
    for z in h:
        if not czy_pierwsza(ord(z)):
            czy_ok = False
            break
    if czy_ok:
        print(h)'''

#zad3.3
ile = [0] * 17
for h in dane:
    licznik = h.count('%') + h.count('!') + h.count('$')
    if licznik == 4:
        print(h)
    ile[licznik] += 1

for i in range(len(ile)):
    print(f'{i}: {ile[i]}')