# m - nr de linii
# n - nr de coloane
from math import floor


def func(a):
    return floor(a * 0.9 + 2)


m = int(input())
n = int(input())

im_originala = []
im_originala_filtrata = []
for _ in range(m):
    for _ in range(n):
        e = int(input())
        im_originala.append(e)
        im_originala_filtrata.append(func(e))

dif = []
for a,b in zip(im_originala_filtrata, im_originala):
    dif.append(a-b)

print(round(sum(dif)/len(dif),2))