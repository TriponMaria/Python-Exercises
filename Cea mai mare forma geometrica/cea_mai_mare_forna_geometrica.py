from math import pi
def arie(tip, dims):
    for j in range(len(dims)):
        dims[j] = float(dims[j])
    if tip == 'patrat':
        arie = dims[0]**2
    elif tip == 'dreptunghi':
        arie = dims[0]*dims[1]
    elif tip == 'cerc':
        arie = pi * (dims[0]**2)
        arie = float(format(arie, '.2f'))

    return tip, arie

n = int(input('Numarul de forme geometrice: '))
arii =[]
forme = []
for i in range(n):
    forma = input('Forma: ').split()
    forme.append(forma)
    arii.append(arie(forma[0], forma[1:]))

maxim = arii[0][1]

for i in range(len(arii)):
    if arii[i][1] > maxim:
        maxim = arii[i][1]

for i in range(n):
    if maxim == arii[i][1]:
        print(' '.join(forme[i]))

# print(arii, maxim)
# print(forme)
