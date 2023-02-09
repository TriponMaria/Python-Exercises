date_intrare = list(map(float, input('n, Pb, Cm: ').split()))
n = int(date_intrare[0])
Pb = date_intrare[1]
Cm = date_intrare[2]
date_vacanta = list(map(int, input('vacanta: ').split()))
zile_vacanta = [date_vacanta[0], date_vacanta[2]]
luna_vacanta = [date_vacanta[1], date_vacanta[3]]

concerte = []
for i in range(n):
    concerte.append(input('Concert: ').split())
concerte_disponibile = []
for i in range(n):
    if not(luna_vacanta[0] <= int(concerte[i][2]) <= luna_vacanta[1] and zile_vacanta[0] <= int(concerte[i][1]) <= zile_vacanta[1]):
        concerte_disponibile.append(concerte[i])

print('concerte disponibile: ', concerte_disponibile)
Pd = []
for i in range(len(concerte_disponibile)):
    Pd.append(int(concerte_disponibile[i][-2])+(2*int(concerte_disponibile[i][-1])*Pb*Cm)/3)

for i in Pd:
    if i == min(Pd):
        idx = Pd.index(i)
        print(concerte_disponibile[idx][0], i)
