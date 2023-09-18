# Lê os valores da peça 1
codigo_peca1, num_peca1, valor_unitario1 = input().split()
codigo_peca1 = int(codigo_peca1)
num_peca1 = int(num_peca1)
valor_unitario1 = float(valor_unitario1)

# Lê os valores da peça 2
codigo_peca2, num_peca2, valor_unitario2 = input().split()
codigo_peca2 = int(codigo_peca2)
num_peca2 = int(num_peca2)
valor_unitario2 = float(valor_unitario2)

# Calcula o valor total a ser pago
total = (num_peca1 * valor_unitario1) + (num_peca2 * valor_unitario2)

# Imprime o resultado
print('VALOR A PAGAR: R$ {:.2f}'.format(total))