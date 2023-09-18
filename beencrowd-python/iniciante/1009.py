nomeV = input('')
salF = float(input(''))
totalV = float(input(''))

comissao = totalV * 0.15
salBruto = comissao + salF

print('TOTAL = R$ {:.2f}'.format(salBruto))