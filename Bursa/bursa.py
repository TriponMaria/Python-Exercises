t = 1
while t:
    try:
        n = input("Introduceti numarul de zile: ")
        n = int(n)
        t = 0
    except ValueError:
        print("n trebuie sa fie int, am primit: ", type(n))

valori = list(map(int,input("Introduceti valorile: ").split()))
#print(valori)


v1 = valori[:-1]
v2 = valori[1:]

func= lambda x,y: x-y

var = list(map(func,v2,v1))
# print(var)
l = [var[0]]
idx = [0]
lista_idx = []
a= 0
liste = []

for j in range(len(var)):
    for i in range(a, len(var)-1):
        #print(f"Compar {var[a]} cu {var[a+1]}")
        if var[a] >= 0 and var[a+1] < 0:
            l.append(var[a+1])
            idx.append(a+1)
            a += 1
        elif var[a] < 0 and var[a+1] >= 0:
            l.append(var[a + 1])
            idx.append(a + 1)
            a += 1
        else:
            liste.append(l)
            lista_idx.append(idx)
            l = [var[a+1]]
            idx = [a+1]
            break
    a += 1
if l:
    liste.append(l)
if idx:
    lista_idx.append(idx)

# print(f'a = {a}')
# print(f'l= {l}')
# print(f'liste= {liste}')
# print(f'lista_idx= {lista_idx}')
max = lista_idx[0]
for i in lista_idx:
    if len(i) >= len(max):
        max = i

secventa =[]
for i in max:
    secventa.append(valori[i+1])



poz = 0
neg = 0
for i in var:
    if i < 0:
        neg += 1
    else:
        poz += 1

if poz == 0 or neg == 0:
    print(0)
else:
    print(f'secventa = {secventa}')
    print('+:' + format((poz*100)/len(var), '.2f') + '%-:' + format((neg*100)/len(var), '.2f')+'%')






