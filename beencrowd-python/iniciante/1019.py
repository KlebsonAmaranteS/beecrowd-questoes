segundos = int(input())

horas = int(segundos // 3600)
segundos %= 3600

minutos = (segundos // 60)
segundos %= 60

segundos_restantes = segundos

tempo_formatado = f"{horas}:{minutos}:{segundos_restantes}"

print(tempo_formatado)