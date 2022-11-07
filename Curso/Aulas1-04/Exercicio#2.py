from random import randint
somal, somac, somad, somad2 = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = randint(1, 10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:>5}', end=" ")
    print()
for j in range(0, 3):
    somal = matriz[0][j] + somal
    somac = matriz[j][0] + somac

if magica + magica1 + magica2 + magica3 == magica:
    print(f'Essa é uma matriz mágica!')
else:
    print(f'Essa não é uma matriz magica')