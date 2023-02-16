import re

text = input('Introduceti textul: ')
n = int(input('Introduceti numarul de cuvinte interzise: '))
cuv_interzise = input('Introduceti cuvintele interzise: ').split()

for cuv in cuv_interzise:
    pattern = cuv
    cautare = re.search(pattern, text)
    if cautare:
        start = cautare.start()
        end = cautare.end()
        text = text.replace(text[start:end], '*'*len(text[start:end]))

print(text)



