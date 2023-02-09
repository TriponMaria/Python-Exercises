ora_s = list(map(int,input("Introduceti ora de sosire: ").split(":")))
n = int(input("Introduceti numarul de autobuze disponibile: "))

ore_autobuze = []
autobuze = []
for i in range(n):
    autobuz = input(f"Autobuz {i+1}: ").split()
    autobuze.append(autobuz)
    autobuz[0] = list(map(int,autobuz[0].split(":")))
    ore_autobuze.append(autobuz[0])
# print(autobuze)

ore_autobuze_disponibile = []
for i in ore_autobuze:
    if ora_s[0] <= i[0] and ora_s[1] <= i[1]:
        ore_autobuze_disponibile.append(i)

for i in range(len(ore_autobuze_disponibile)-1):
    if ore_autobuze_disponibile[i+1][0] < ore_autobuze_disponibile[i][0]:
        del ore_autobuze_disponibile[i]

for i in range(len(ore_autobuze_disponibile)-1):
    if ore_autobuze_disponibile[i+1][1] > ore_autobuze_disponibile[i][1]:
        del ore_autobuze_disponibile[i+1]
# print(ore_autobuze_disponibile)

autobuze_posibile = []
idx = []
for i in range(n):
    if autobuze[i][0] == ore_autobuze_disponibile[0]:
        autobuze_posibile.append(autobuze[i])

# print(autobuze_posibile)
preturi = []
for i in range(len(autobuze_posibile)):
    preturi.append(int(autobuze_posibile[i][1]))

preturi.sort()
for i in range(len(autobuze_posibile)):
    if int(autobuze_posibile[i][1]) == preturi[0]:
        print(f"O sa calatoresc cu {autobuze_posibile[i][2]}")






