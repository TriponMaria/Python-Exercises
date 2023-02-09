n = int(input('Numarul de dreptunghiuri desenate: '))
dreptunghiuri = []
maxim = 0
for i in range(n):
    dreptunghi = input('Dreptunghi: ').split()
    for i in range(1,len(dreptunghi)):
        dreptunghi[i] = int(dreptunghi[i])
    l1 = dreptunghi[4] - dreptunghi[2]
    l2 = dreptunghi[3] - dreptunghi[1]
    arie = l1 * l2
    dreptunghi.append(arie)
    dreptunghiuri.append(dreptunghi)
    if arie > maxim:
        maxim = arie

rezultat = ''
for i in range(n):
    if maxim == dreptunghiuri[i][5]:
        for i in dreptunghiuri[i]:
            rezultat += str(i) + ' '

print(rezultat)