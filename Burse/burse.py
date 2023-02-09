prima_linie = list(map(int, input("m, n, p: ").split()))
m = prima_linie[0]
n = prima_linie[1]
p = prima_linie[2]
nume_medie =[]
for i in range(m):
    nume = input('Nume student: ')
    note = list(map(int, input('Note: ').split()))
    suma_note = 0
    for nota in note:
        if nota >=5:
            suma_note += nota
        else:
            suma_note = 0
            break
    medie = float(format(suma_note/len(note), '.2f'))
    if medie != 0.00 and medie >= 8.00:
        nume_medie.append([nume,medie])

# print(f'nume_medie = {nume_medie}')
performanta = nume_medie[0][1]
for i in range(1,len(nume_medie)):
    if nume_medie[i][1] > performanta:
        performanta = nume_medie[i][1]
        student_performanta = nume_medie[i]
        r = nume_medie[i]
nume_medie.remove(r)
if len(nume_medie) >= p:
    print(p)
else:
    print(len(nume_medie))

print(f"{student_performanta[0]} {student_performanta[1]}")
