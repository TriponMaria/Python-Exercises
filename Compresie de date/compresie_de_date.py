n = int(input('Numarul de linii de date: '))
rezultat = []
for i in range(n):
    lista = list(map(int, input('Date: ').split(',')))
    lista2 = []
    for i in range(len(lista) - 1):
        if lista[i] != 0 and lista[i + 1] != 0:
            lista2.append(lista[i])
        elif lista[i] != 0 and lista[i + 1] == 0:
            count = 0
            for j in range((i + 1), len(lista)):
                if lista[j] == 0:
                    count += 1
                else:
                    break
            lista2.append((lista[i], count))
    if lista[-1] != 0:
        lista2.append(lista[-1])
    rezultat.append(lista2)

for i in rezultat:
    print(i)
