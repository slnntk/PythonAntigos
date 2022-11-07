d = int(input('Qual a distancia percorrida da viagem em km? '))

if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45

print(f'O preço da sua passagem na viagem de {d} vai ser de {p}')
    