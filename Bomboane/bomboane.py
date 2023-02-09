n = int(input("Nr de zile: "))
bani = list(map(int,input("Suma zilnica: ").split()))
cost_aroma = []
for i in range(n):
    cost_aroma.append(list(map(int, input("Cost si aroma bomboana: ").split())))

print(cost_aroma)

pct_fericire_anterioare = []
pct_fericire = 0
bani_ramasi = 0
for i in range(n):
    pct_fericire_anterioare.append(cost_aroma[i][1])
    bani[i] += bani_ramasi
    bani_ramasi = 0
    if cost_aroma[i][0] <= bani[i]:
        pct_fericire += cost_aroma[i][1]
        bani_ramasi = bani[i] - cost_aroma[i][0]
    else:
        for j in pct_fericire_anterioare:
            if cost_aroma[i][1] > j:
                pct_fericire -= cost_aroma[i][1]
                break
print("Puncte de fericire: ", pct_fericire)
