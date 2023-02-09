text = input('Text: ')
n = int(input('Numarul de chei criptare(n): '))
chei = []
for i in range(n):
    cheie = int(input('Cheie: '))
    chei.append(cheie)

alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','M',
           'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabet_L =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','m',
           'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


keys = []
litere = []
for l in text:
    if l.upper() in alfabet:
        litere.append(l)

a = True
while a:
    for c in chei:
        if len(keys) <= len(litere):
            keys.append(c)
            if len(keys) == len(litere):
                a = False
                break


print(keys)
print(litere)
mesaj_criptat = ''
i = 0
for l in text:
    if l in alfabet:
        if alfabet.index(l) + keys[i] > len(alfabet) - 1:
            cheie = (alfabet.index(l) + keys[i]) - (len(alfabet) - 1)
            mesaj_criptat += alfabet[cheie - 1]
            i += 1
        else:

            mesaj_criptat += alfabet[alfabet.index(litere[i]) + keys[i]]
            i += 1
    elif l in alfabet_L:
        if alfabet_L.index(l) + keys[i] > len(alfabet_L) - 1:
            cheie = (alfabet_L.index(l) + keys[i]) - (len(alfabet_L) - 1)
            mesaj_criptat += alfabet_L[cheie - 1]
            i += 1
        else:
            mesaj_criptat += alfabet_L[alfabet_L.index(litere[i]) + keys[i]]
            i += 1
    else:
        mesaj_criptat += l

print(mesaj_criptat)