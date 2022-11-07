matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = col = par = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor que está em {[l]}, {[c]}: '))
        if matriz[l][c] % 2 == 0:
            par = par + matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")
    print()
print(f'A soma de todos os valores pares é de {par} ')
for l in range(0, 3):
    col = col + matriz[l][2]
print(f'A soma dos valores da terceira coluna é {col}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
