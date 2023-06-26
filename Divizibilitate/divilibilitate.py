k = int(input("k: "))
lista_nr = []

lungimi = []
sume = []
lungimi_sume = []
max_lungime = 0
suma_max = 0
a = 2

for _ in range(k):
    nr = input("nr: ")
    lista_nr.append(int(nr))

for j in range(k):
    for i in range(a, k + 1):
        if sum(lista_nr[j:i]) % 3 == 0:
            lungimi.append(len(lista_nr[j:i]))
            lungimi_sume.append([sum(lista_nr[j:i]), len(lista_nr[j:i])])
    a += 1

if lungimi:
    max_lungime = max(lungimi)
    for ls in lungimi_sume:
        if ls[1] == max_lungime:
            sume.append(ls[0])

    suma_max = max(sume)


if max_lungime == 0:
    print(0)
else:
    print(max_lungime, suma_max)