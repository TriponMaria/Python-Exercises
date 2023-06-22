nr_linii = int(input("Nr linii: "))
lista_culori = input("Lista culori: ").split()
rezultat = []
for i in range(nr_linii-1):
    copil = input("Copil: ").split()
    rezultat.append(copil[0])
    culori_copil = copil[2:]

    if 'red' and 'blue' in lista_culori and 'purple' not in lista_culori:
        lista_culori.append('purple')
    if 'yellow' and 'red' in lista_culori and 'orange' not in lista_culori:
        lista_culori.append('orange')
    if 'yellow' and 'blue' in lista_culori and 'green' not in lista_culori:
        lista_culori.append('green')
    if 'red' and 'yellow' and 'blue' in lista_culori and 'brown' not in lista_culori:
        lista_culori.append('brown')

    for culoare in culori_copil:
        if culoare not in lista_culori:
            rezultat.remove(copil[0])

print('\n'.join(rezultat))
