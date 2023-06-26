n = int(input("Numarul de emotii detectate: "))

emotii = dict()
angajati = []
for _ in range(n):
    emotie = input("Emotie: ").split()
    emotie[1] = int(emotie[1])
    emotii[emotie[0]] = emotie[1]

joburi = []
for _ in range(5):
    angajat = input("Angajat: ").split()
    angajati.append(angajat[1:])
    joburi.append(angajat[2])

joburi = list(set(joburi))
d = dict()
for job in joburi:
    emotii_angajat = []
    for angajat in angajati:
        if angajat[1] == job:
            emotii_angajat.append(emotii[angajat[0]])
    d[job] = round(sum(emotii_angajat) / len(emotii_angajat), 2)

for key in d.keys():
    print(f"{key} {d[key]}")
