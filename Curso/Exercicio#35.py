n1 = int(input('Digite o primeiro lado: '))
n2 = int(input('Digite o segundo lado: '))
n3 = int(input('Digite o terceiro lado: '))

if n1 < n3+n2 and n2 < n3+n1 and n3 < n1+n2:
    print(f'Esse triangulo é possível.')
else:
    print(f'Esse triangulo é impossível.')
