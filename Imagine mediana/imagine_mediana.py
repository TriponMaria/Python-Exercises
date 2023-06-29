def A_0_func(A):
    A.insert(0, [0 for _ in range(m + 2)])
    A.append([0 for _ in range(m + 2)])
    for line in A:
        if len(line) == m:
            line.insert(0, 0)
            line.append(0)
    return A


m = int(input())
n = int(input())
A = []
for i in range(m):
    linie = []
    for j in range(n):
        linie.append(int(input()))
    A.append(linie)

A_0 = A_0_func(A)

A_f = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = []
for j in range(1, m + 1):
    linie = []
    for i in range(1, n + 1):
        linie = [A_0[i - 1][j], A_0[i][j - 1], A_0[i][j], A_0[i][j + 1], A_0[i + 1][j]]
        linie.sort()
        if linie:
            a.append([i - 1, j - 1, linie[2]])

for i in a:
    A_f[i[0]][i[1]] = i[2]

for i in range(m):
    for j in range(n):
        print(A_f[i][j])
