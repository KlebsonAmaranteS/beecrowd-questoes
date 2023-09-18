codigo, quantidade = map(int, input().split(' '))

cachorro_quente = 4.00
x_salada = 4.50
x_bacon = 5.00
torrada = 2.00
refri = 1.50


if codigo == 1:
    valor = cachorro_quente * quantidade
    print(f'Total: R$ {valor:.2f}')
elif codigo == 2: 
    valor = x_salada * quantidade
    print(f'Total: R$ {valor:.2f}')
elif codigo == 3: 
    valor = x_bacon * quantidade
    print(f'Total: R$ {valor:.2f}')
elif codigo == 4:
    valor = torrada * quantidade
    print(f'Total: R$ {valor:.2f}')
elif codigo == 5:
    valor = refri * quantidade
    print(f'Total: R$ {valor:.2f}')