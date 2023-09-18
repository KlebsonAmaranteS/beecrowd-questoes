idade = int(input())

ano = int(idade / 365)
idade %= 365

mes = int(idade / 30)
idade %= 30

dias = idade 

print(f'{ano} ano(s)\n{mes} mes(es)\n{dias} dia(s)')