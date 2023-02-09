import math
m = int(input('Numar linii: '))
n = int(input('Numar coloane: '))
matrice = []
for i in range(m):
    e = []
    for j in range(n):
        e.append(int(input('e: ')))
    matrice.append(e)
print(matrice)

def coef1(u):
    if u == 0:
        return 1/math.sqrt(m)
    elif u > 0:
        return math.sqrt(2/m)

def coef2(v):
    if v == 0:
        return 1/math.sqrt(n)
    elif v > 0:
        return math.sqrt(2/n)

def suma(m,n):
    sume =[]
    for u in range(m):
        for v in range(n):
            suma = 0
            for i in range(m):
                for j in range(n):
                    suma += math.cos(3.14*u/(2*m)*(2*i + 1))*math.cos(3.14*v/(2*n)*(2*j + 1))*matrice[i][j]
            sume.append(coef1(u)*coef2(v)*suma)
    return sume

print('sume: ', suma(m,n))
Af = []
Af.append([suma(m,n)[0],0,0])
for i in range(1,m):
    a = []
    for j in range(n):
        a.append(0)
    Af.append(a)
# print('Af: ',Af)
Ar = []
for i in range(m):
    for j in range(n):
        suma = 0
        for u,v in zip(range(m), range(n)):
            # print('u ', u)
            # print('v ', v)
            # print(Af[u][v])
            suma += coef1(u)*coef2(v)*math.cos((math.pi*u/2*m)*(2*i + 1))*math.cos((math.pi*v/2*n)*(2*j + 1))*Af[u][v]
        Ar.append(suma)

# print('Ar: ', Ar)
for i in Ar:
    print(math.floor(i))








