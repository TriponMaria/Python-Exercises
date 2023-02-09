n = int(input("Introduceti numarul de loturi: "))

util_inutil = []
for i in range(n):
    k = int(input("Nr componente lot: "))
    lot = str(input("Lotul: ")).split()
    nr_S = lot.count("S")
    nr_P = lot.count("P")
    nr_R = lot.count("R")
    nr_H = lot.count("H")
    nr_B = lot.count("B")
    print(nr_S, nr_P, nr_R, nr_H, nr_B)
    if nr_S== nr_P and nr_R % 4 == 0 and nr_R != 0 and nr_H % 2 == 0 and nr_H != 0 and nr_H <= 2 and nr_B % 2 == 0 and nr_B != 0 :
        util_inutil.append(1)
    else:
        util_inutil.append(0)

print(f'Numarul de loturi utile, respectiv inutile: {util_inutil.count(1)}, {util_inutil.count(0)}')
print(f"{util_inutil}")
pondere = util_inutil.count(1)/util_inutil.count(0)
print(pondere)




