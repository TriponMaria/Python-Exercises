from math import factorial
k = int(input("k: "))
M = int(input("M: "))

def Aranjamente(n,k):
    return factorial(n)/factorial(n-k)

n = k
maxim = 0
while Aranjamente(n, k) <= M:
    if Aranjamente(n, k) <= M:
        maxim = n
        n += 1

print(maxim)


