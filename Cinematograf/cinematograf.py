ora = input('Ora la care ajungeti la cinema: ').split(':')
ora_ajungere = int(ora[0]+ora[1])
n = int(input('Introduceti numarul de filme: '))
ore_start =[]
preturi = []
filme = []
for i in range(n):
    film = input('Film: ').split()
    filme.append(film)
    o = film[0].split(':')
    ore_start.append(int(o[0]+o[1]))
    preturi.append(film[1])

index = []
for o in ore_start:
    if o < ora_ajungere:
        index.append(ore_start.index(o))

filme = [i for j, i in enumerate(filme) if j not in index]
ore_start = [i for j, i in enumerate(ore_start) if j not in index]
preturi = [i for j, i in enumerate(preturi) if j not in index]

# print('filme: ', filme)
# print('ore_start: ', ore_start)
# print('preturi: ', preturi)
diferente = []
index = []
for o in range(len(ore_start)):
    diferenta = ore_start[o] - ora_ajungere
    diferente.append(diferenta)
minim = min(diferente)
# print('minim: ', minim)
for i in diferente:
    if i != minim:
        index.append(diferente.index(i))
# print('diferente: ', diferente)
# print('index: ', index)
filme = [i for j, i in enumerate(filme) if j not in index]
ore_start = [i for j, i in enumerate(ore_start) if j not in index]
preturi = [i for j, i in enumerate(preturi) if j not in index]
pret_minim_index = [preturi.index(min(preturi))]
print(filme[pret_minim_index[0]][2])








