n1 = int(input('Digite o numero do primeiro lado do triangulo: '))
n2= int(input('Digite o numero do segundo lado do triangulo: '))
n3 = int(input('Digite o numero do terceiro lado do triangulo: '))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n2 + n1:
    print(f'O triangulo de lados {n1, n2, n3} é possível')
    if n1 == n2 == n3:
        print(f'O triangulo supracitado é equilátero')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print(f'O triangulo supracitado é isosceles!')
    else:
        print(f'O triangulo supracitado é escaleno!')



else:
    print(f'O triangulo é impossivel:')



