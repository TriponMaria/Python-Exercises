prima_linie = list(map(int, input('n si k: ').split()))
n = prima_linie[0]
k = prima_linie[1]
nr = list(map(int, input('nr: ').split()))

nr_k = []
for i in range(n):
    if nr[i] >= k:
        nr_k.append(nr[i])

# print('nr: ', nr_k)
nr_k.sort()
nr_f = []
for i in range(len(nr_k)):
    for j in range(2,nr_k[i]):
        if nr_k[i] %  j == 0:
            nr_f.append(nr_k[i])
rez = []
for i in nr_k:
    if i not in nr_f:
        rez.append(i)

# print('nr_f',rez)
if rez:
    print(rez[0])
else:
    print('-1')