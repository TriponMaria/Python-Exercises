import datetime

ora_aj = input("Ora la care ajungeti: ")
ora_aj = datetime.datetime.strptime(ora_aj, '%H:%M').time()
n = int(input('n: '))
ghisee = [input("Ghiseu: ").split() for _ in range(n)]
ghisee = [ghiseu for ghiseu in ghisee if ora_aj < datetime.datetime.strptime(ghiseu[0], '%H:%M').time()]
ore_ghisee = [ghiseu[0] for ghiseu in ghisee]
ora_ghiseu_min = min(ore_ghisee)
ghisee_filtrate = [ghiseu for ghiseu in ghisee if ghiseu[0] == ora_ghiseu_min]

if len(ghisee_filtrate) != 1:
    nr_min_dislikes = int(ghisee_filtrate[0][1])
    rezultat = [ghisee_filtrate[0]]
    for ghiseu in ghisee:
        if int(ghiseu[1]) < nr_min_dislikes:
            nr_min_dislikes = int(ghiseu[1])
            rezultat.append(ghiseu)
    print(rezultat[0][2])
else:
    print(ghisee_filtrate[0][2])


