np =list(map(int, input("PS si Pf nava proprie: ").split()))
n = int(input("Introduceti numarul de nave inamice: "))
ni = []
s = 0
for i in range(n):
    ni = list(map(int,input(f"Nava inamica {i}: ").split()))
    c = 0
    while (np[0]-ni[1]) >= 0 and (ni[0] - np[1]) >=0:
        np[0] -= ni[1]
        ni[0] -= np[1]
        c += 1
        print(np, ni,c)
    if c % 2 != 0:
        s += 1
print(s)
