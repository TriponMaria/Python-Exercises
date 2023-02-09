prima_linie = list(map(int,input("Introduceti latura matricei si nr de valori strigate: ").split()))
n = prima_linie[0]
k = prima_linie[1]
nr_bunica = list(map(int, input("Introduce numerele bunicii: ").split()))
nr_bingo = list(map(int, input("Numere bingo: ").split()))
a = 0
b = 0
for i in set(nr_bingo):
    if i in nr_bunica:
        a += 1


if a == (n*n):
    print("Bingo")
else:
    print(len(nr_bunica)-a)
