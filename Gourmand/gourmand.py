from numpy import prod
from math import sqrt

n = int(input())
dict_emotii = dict()
for n in range(n):
    emotie = input().split()
    dict_emotii[emotie[0]] = int(emotie[1])

oameni = []
medii_dict = dict()
for i in range(5):
    om = input().split()
    oameni.append(om)
    if om[2] in medii_dict.keys():
        medii_dict[om[2]].append(dict_emotii[om[1]])
    else:
        medii_dict[om[2]] = [dict_emotii[om[1]]]

print(medii_dict)
medii_dict = {key: sqrt(prod(medii_dict[key]))for key in medii_dict.keys()}

for key in medii_dict.keys():
    print(f"{key} {round(medii_dict[key], 2)}")