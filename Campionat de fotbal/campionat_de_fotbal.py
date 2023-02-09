k = int(input('Numar echipe: '))
n = int(input('Numarul de meciuri: '))
meciuri = []
for i in range(n):
    meci = list(input('Meci: ').split())
    for i in meci:
        if i == '-':
            meci.remove(i)
        try:
            i = int(i)
        except ValueError:
            pass
    meciuri.append(meci)

#print(meciuri)
echipe = []
for i in range(n):
    meciuri[i][1] = int(meciuri[i][1])
    meciuri[i][2] = int(meciuri[i][2])
    echipe.append(meciuri[i][0])
    echipe.append(meciuri[i][3])

echipe = list(set(echipe))
print("echipe: ", echipe)
rezultat = []
for e in echipe:
    puncte = 0
    goluri_date = 0
    goluri_primite = 0
    for m in range(n):
        if e == meciuri[m][0]:
            if meciuri[m][1] > meciuri[m][2]:
                puncte += 3
                goluri_date += meciuri[m][1]
                goluri_primite += meciuri[m][2]
            elif meciuri[m][1] < meciuri[m][2]:
                goluri_date += meciuri[m][1]
                goluri_primite += meciuri[m][2]
            elif meciuri[m][1] == meciuri[m][2]:
                puncte += 1
                goluri_date += meciuri[m][1]
                goluri_primite += meciuri[m][2]
        elif e == meciuri[m][3]:
            if meciuri[m][1] < meciuri[m][2]:
                puncte += 3
                goluri_date += meciuri[m][2]
                goluri_primite += meciuri[m][1]
            elif meciuri[m][1] > meciuri[m][2]:
                goluri_date += meciuri[m][2]
                goluri_primite += meciuri[m][1]
            elif meciuri[m][1] == meciuri[m][2]:
                puncte += 1
                goluri_date += meciuri[m][1]
                goluri_primite += meciuri[m][2]

    rezultat.append([e,puncte,goluri_date, goluri_primite])

print(rezultat)
for i in range(len(rezultat)):
    for j in range(len(rezultat)-i-1):
        if rezultat[j][1] < rezultat[j+1][1]:
            temp = rezultat[j]
            rezultat[j] = rezultat[j+1]
            rezultat[j+1] = temp

print(rezultat)


