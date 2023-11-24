hora_inicial, hora_final = map(int, input().split(" "))

diferenca_horas = hora_final - hora_inicial

if diferenca_horas <= 0:
    diferenca_horas += 24  
print(f"O JOGO DUROU {diferenca_horas} HORA(S)")

