import random
def m():
    soma = 0
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] = random.randint(0, 100)


    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l][c]:^5}]', end=" ")
        print()

        soma = matriz[0][0] + matriz[0][1] + matriz[0][2]
        for l in range(1, 3):
            for c in range(1, 3):
                if matriz[l][c] + matriz[l][c] + matriz[l][c] > soma:
                    soma = matriz[l][c] + matriz[l][c] + matriz[l][c]

    print(f'A linha com a maior soma é {soma}')



m()



