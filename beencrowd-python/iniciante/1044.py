a, b = map(int, input().split(" "))

maior_valor = max(a, b)
menor_valor = min(a, b)
a = maior_valor
b = menor_valor

if a % b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")