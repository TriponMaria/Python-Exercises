from operator import add
stoc = list(map(int,input("Introduceti stocul atelierului: ").split()))
l = int(input("Introduceti nr de laptopuri care intra in service: "))

laptop = []
func = lambda x, y: x + y
n = 0
piese_defecte = []
for i in range(l):
    laptop = list(map(int,input(f"Laptop {i+1}: ").split()))
    m = 0
    for i in range(len(stoc)):
        if stoc[i] == 0 and laptop[i] == 0:
            stoc = list(map(func, stoc, laptop))
            n += 1
            m += 1
    if m ==0:
        for i in range(len(stoc)):
            if stoc[i] != 0 and laptop[i] == 0:
                stoc[i] -= 1
    print(stoc)


print("Numar laptopuri reparate: ", l-n)
