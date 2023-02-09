def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

intrari = list(map(int,input('n si M: ').split()))
n = intrari[0]
M = intrari[1]
k = 1
while True:
    c = factorial(n)/(factorial(k)*factorial(n-k))
    if c >= M:
        print(k)
        break
    k += 1
    if k == n:
        print(0)
        break