def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    count = i
    if i < f:
        while count <= f:
            if count == f:
                print(f'{count}', end=" ")
            else:
                print(f'{count},', end=" ")
            count += p
        print('\nFim')
    else:
        while count >= f:
            if count == f:
                print(f'{count}', end=" ")
            else:
                print(f'{count},', end=" ")
            count -= p



print('Contagem')
a = int(input('Começando em : '))
b = int(input('Terminando em : '))
c = int(input('De : '))
contador(a, b, c)