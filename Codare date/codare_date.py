n = int(input("Numarul de valori intregi pozitive(n): "))
sume = []
for i in range(n):
    nr = list(map(int,input('Nr: ').split()))
    nr_prim = []
    nr_prim_pare = []
    nr_prim_impare = []
    for j in range(len(nr)):
        if j % 2 == 0:
            nr_prim_pare.append(nr[j])
        else:
            nr_prim_impare.append(nr[j])
    for i,j in zip(nr_prim_impare, nr_prim_pare):
        nr_prim.append(i)
        nr_prim.append(j)
    nr_prim.append(nr[-1])
    nr_secund = []
    nr_secund.append(nr_prim[0])
    for s in nr_prim[1:]:
        while True:
            s = s % 2
            if s == 0:
                nr_secund.append(s)
                break
            elif s == 1:
                nr_secund.append(s)
                break
    sume.append(sum(nr_secund))

print(sume)
print(max(sume))
