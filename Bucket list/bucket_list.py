n = int(input("Numar de valori de pe a doua linie: "))
numere = input("Introduceti valorile: ").split()
dim = []
for i in numere:
    dim.append(len(i))

dim.sort()
for i in set(dim):
    print(i, dim.count(i))