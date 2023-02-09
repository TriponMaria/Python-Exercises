from math import sqrt
prima_linie = list(map(int,input('n, k, Mc, Rc, Gc, Bc: ').split()))
n = prima_linie[0]
date_fructe = prima_linie[2:]
tipuri_fructe = []
distante = []
for i in range(n):
    fruct = list(map(int, input('Fruct: ').split()))
    tipuri_fructe.append(fruct[0])
    fruct = fruct[1:]
    suma = 0
    for i in range(len(fruct)):
        suma += (date_fructe[i]-fruct[i])**2
    distanta = sqrt(suma)
    distante.append(distanta)

print(tipuri_fructe[distante.index(min(distante))])
print(min(distante))
