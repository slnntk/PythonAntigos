valores= list()
for c in range(0, 5):
    valores.append(int(input(f'Digite aqui o seu valor na posição {c}:  ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print(f'\nVocê digitou os valores {valores}')
print(f'O maior valor é o valor: {mai} nas posições:', end=" ")
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...',end=" ")
print(f'\nO menor valor é o valor: {men}: ', end=" ")
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end=" ")

