text = input('Text: ')
dictionar = input("Dictionar: ").split()
l1 = []
l2 = []
for d in dictionar:
    d = d.split(',')
    l1.append(d[0]) #caracterele ce au inlocuitor
    l2.append(d[1]) #caracterele ca vor inlocui caracterele din lista l1 cu acelasi index


#print(perechi)
text_criptat = ''
for l in text:
    if l in l1:
        text_criptat += l2[l1.index(l)]
    else:
        text_criptat += l

print(text_criptat)
