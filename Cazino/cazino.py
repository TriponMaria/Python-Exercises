n = int(input('Numarul de carti jucate: '))
carti = []
for i in range(n):
    carte = input('Carte: ').split()
    carti.append(carte)

trisoare = []
for i in carti:
    if carti.count(i) == 3 and i not in trisoare:
        trisoare.append(i)
idxs = []
#print(trisoare)
for i in trisoare:
    idx = []
    for j in range(n):
        if i == carti[j]:
            idx.append(j)
    #print(idx)
    idxs.append(idx[2])

idxs.sort()
#print(idxs)
if idxs:
    print(' '.join(carti[idxs[0]]))
else:
    print('JOC OK')