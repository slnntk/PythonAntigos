i = int(input('Inicio do intervalo: '))
f = int(input('Final do intervalo: '))
print(f'Os numros pares no intervalo de {i} a {f} é igual a : ')
for c in range(i+1, f+1, 2 ):
    if c % 2 == 0:
        print(f'{c}', end= " ")