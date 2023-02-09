nr_valori = int(input('Numarul de valori intregi: '))
nr_zerouri = []
numere = []
for i in range(nr_valori):
    n = int(input('n: '))
    numere.append(n)
    resturi = []
    while True:
        resturi.append(n % 2)
        n = n // 2
        if n == 0:
            break
    if len(resturi) != 8:
        zerouri = []
        for i in range(8 - len(resturi)):
            zerouri.append(0)
        resturi = zerouri + resturi
    #print(resturi)
    nr_zerouri.append(resturi.count(0))

# print(nr_zerouri)
for i in range(nr_valori):
    if nr_zerouri[i] == max(nr_zerouri):
        print(numere[i])








