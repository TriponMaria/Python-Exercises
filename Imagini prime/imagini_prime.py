# m - nr de linii
# n - nr de coloane
def nr_prim(a):
    for i in range(2, a):
        if a % i == 0 or a == 0 or a == 1:
            return False
    return True


m = int(input())
n = int(input())
im_originala = []
for _ in range(m):
    for _ in range(n):
        im_originala.append(int(input()))

print(im_originala)

ones = []
for nr in im_originala:
    if not nr_prim(nr):
        ones.append(1)

print(len(ones))