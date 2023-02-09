n = int(input('Nr de valori inregistrate(n): '))
date = list(map(int, input('Date: ').split()))

def secvente(l):
    a = 0
    rez = [l[0]]
    rezultat = []
    for i in range(len(l)):
        for j in range(a, len(l)-1):
            if l[a] < 0 and l[a+1] >= 0:
                rez.append(l[a+1])
                a += 1
            elif l[a] >= 0 and l[a+1] < 0:
                rez.append(l[a+1])
                a += 1
            else:
                rezultat.append(rez)
                rez = [l[a+1]]
                break
        a += 1
    return rezultat
rezultat = secvente(date)
m = len(rezultat[0])
afisare = []
for i in rezultat:
    if len(i) >= m:
        m = len(i)
        afisare = i
neg = 0
poz = 0
for i in date:
    if i < 0:
        neg += 1
    else:
        poz += 1
print(len(afisare))
print(afisare)
print(f'+:{((poz/n)*100):.2f}% -:{(neg/n*100):.2f}%')