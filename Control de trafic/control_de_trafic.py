n = int(input('Numar autobuze(n): '))
autobuze = list(map(int, input('Autobuze: ').split()))
autobuze_posibile = list(range(1,n+1))
suma = 0
for i in autobuze_posibile:
    if i not in autobuze:
        suma += i

print(suma)