licznik = 0
def tablica(A, i, n):
    global licznik
    licznik += 1
    if i == n * n:
        return 0
    w = (i // n)
    k = (i % n)
    return A[w][k] + tablica(A, i + 1, n)
"""A = [[2, 1], [5, 3]]
i = 0
print(tablica(A, i, 2))"""

A = [[[2, 1], [5, 3]], [[3, 4], [5, 1]], [[1, 2, 1], [3, 1, 1], [2, 1, 4]]]
i = [0, 0, 0]
n = [2, 2, 3]

for x in range(3):
    licznik = 0
    print(tablica(A[x], i[x], n[x]), licznik)

#ODP: 1.F 2.F 3.P
#zad1.3
def tablica2(A, i, n):
    for x in A:
        suma = 0
        for y in x:
            suma += sum(y)
        print(suma)
tablica2(A, i, n)
'''A0 = [[2, 1], [5, 3]]
def tablica2_2(A0, i, n):
    suma = 0
    j = 0
    while j < n:
        k = 0
        while k < n:
            suma += A0[j][k]
            k += 1
        j += 1
tablica2_2(A0, i ,n)
print(suma)'''
