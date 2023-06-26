n = int(input("n: "))
l_list = []
forma = []
for i in range(n):
    pct = list(map(float, input('Punct: ').split()))
    forma.append(pct)
    l = pct[0] - pct[1]
    if l < 0:
        l_list.append(l * -1)
    else:
        l_list.append(l)

if len(set(l_list)) == 1 or (len(set(l_list)) == 2 and n == 4):
    print('da')
else:
    print('nu')
