import math
n = int(input('Numar de elemente din vector: '))
v =[]
for i in range(n):
    val = int(input("v: "))
    v.append(val)
x = int(input('Valoarea care va fi cautata: '))
# print(f'v= {v}')
v.sort()
a = n
c = True
while a != 1:
    print(v[math.floor(a / 2)])
    if x == v[math.floor(a/2)]:
        break
    elif math.floor(a/2) == 1:
        break
    elif x < v[math.floor(a/2)]:
        if math.floor(a/2) % 2 == 1 :
            v = v[0:math.floor(a/2)-1]
            a = math.floor(a/2)
            # print(f"v1:{v}, a = {a}")
        else:
            v = v[0:math.floor(a / 2)]
            a = math.floor(a / 2)
            # print(f"v1:{v}, a = {a}")
    elif x > v[math.floor(a/2)]:
        if math.floor(a/2) % 2 == 1:
            v = v[math.floor(a / 2) + 1:]
            a = math.floor(a / 2)
            # print(f"v1:{v}, a = {a}")
        else:
            v = v[math.floor(a / 2):]
            a = math.floor(a / 2)
            # print(f"v1:{v}, a = {a}")

if math.floor(a/2) == 1 and x != v[math.floor(a / 2)]:
        print(v[0])





