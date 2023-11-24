a, b, c = map(float, input().split(" "))
valores = [a, b, c]

if a + b > c and a + c > b and b + c > a:
    soma_perimetro = sum(valores)
    print(f"Perimetro = {soma_perimetro:.1f}")
else:
    menor_valor = min(valores)
    remove_menor_valor = valores.remove(menor_valor)
    soma_valores_area = sum(valores)
    print(f"Area = {soma_valores_area:.1f}")
    