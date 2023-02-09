prima_linie = list(map(int, input("Dimensiune raft si numarul tipurilor de carti disponibile: ").split()))
dr = prima_linie[0]
k = prima_linie[1]
cd = []
for i in range(k):
    cd.append(list(map(int,input("Numar carti de numar pagini: ").split())))
#print(cd)

rafturi = []
for i in range(k):
    for j in range(k):
        while cd[i][1] + cd[j][1] <= dr and cd[i][0] > 0 and cd[j][0] > 0:
            raft = []
            raft.append(cd[i][1])
            raft.append(cd[j][1])
            cd[i][0] -= 1
            cd[j][0] -= 1
            suma = cd[i][1] + cd[j][1]
            while suma + cd[j][1] <= dr and cd[i][0] > 0 and cd[j][0] > 0:
                raft.append(cd[j][1])
                cd[j][0] -= 1
                suma += cd[j][1]
            if raft:
                rafturi.append(raft)

print(rafturi)











