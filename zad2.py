#zad2.3
def horner(n, a, A):
    wynik = A[0]
    for i in range(n - 1, -1, -1): #od n-1 do 0 co -1(malejąco co 1)
        wynik = wynik * a + A[n - i]
    return wynik

A = [2, 5, 7, 9]
n = len(A) - 1
#print(horner(n, 1, A))

#zad2.4
dane = [list(map(int, w.split()))[1:] for w in open('wielomiany.txt')]

max_r = 0
max_w = []

'''for w in dane:
    n = len(w) - 1
    l_mn_tr = n * (n + 1) / 2
    l_mn_hr = n
    r = l_mn_tr - l_mn_hr
    if r == max_r:
        max_w.append(w)
    elif r > max_r:
        max_r = r
        max_w = [w]


#max_w = max_w.insert(0, len(max_w) - 1)
for w in max_w:
    w = [len(max_w) - 1] + w
    print(w)
print(max_r)'''

#zad2.5
def fib():
    wynik = [1, 1]
    for i in range(2, 101):
        wynik.append(wynik[i-2] + wynik[i-1])
    return wynik

ciag_fib = fib()

for w in dane:
    w_od_2 = horner(len(w) - 1, 2, w)
    if w_od_2 in ciag_fib:
        print([len(w) - 1] + w)