prima_line = list(map(int, input("n si p: ").split()))
valorile_presiunii = list(map(float, input("Valorile presiunii: ").split()))

n = prima_line[1]
p = prima_line[0]
while n:
    valorile_presiunii.append(round(sum(valorile_presiunii) / p, 2))
    valorile_presiunii.remove(valorile_presiunii[0])
    n -= 1

valori_progmozate = valorile_presiunii[-n + 1:]
diferenta_max_min = max(valori_progmozate) - min(valori_progmozate)
valori_progmozate = [str(val) for val in valori_progmozate]
print(' '.join(valori_progmozate))
print(round(diferenta_max_min, 2))
