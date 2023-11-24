x, y, z = map(int, input().split(' '))

valores = [x, y, z]
lista_valor = valores.copy()
valores.sort()

for valor in valores:
    print(valor)
print()
for valor2 in lista_valor: 
    print(valor2)