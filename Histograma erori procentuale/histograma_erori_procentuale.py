optim = int(input())
valori = list(map(int, input().split()))

p = 0
iesire = dict()

for i in range(0,105,5):
    if i == 100:
        key = f"{i}%+"
    else:
        key = f"[{i}% - {i+5}%)"
    iesire[key] = 0
    for val in valori:
        eroare = (val * 100) / optim - 100
        if i <= eroare < i+5:
            iesire[key] += 1

for key in iesire.keys():
    print(f"{key} = {iesire[key]}")
