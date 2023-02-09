m = int(input('m: '))
n = int(input('n: '))
v1 = []
for i in range(m*n):
    v1.append(int(input("> ")))

#print(len(v1) - (len(set(v1))*2))

v1.sort()
v2 = []

for i in set(v1):
    v2.append([i,v1.count(i)])
v2_final = []

for j in v2:
    v2_final += j
print('v2 = ', v2)
print(len(v1) - len(v2_final))