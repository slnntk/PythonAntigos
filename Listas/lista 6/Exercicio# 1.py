matriz = [[], [], [], [], []],[[], [], [], [], []],[[], [], [], [], []], [[], [], [], [], []] ,[[], [], [], [], []]
for l in range(0, 5):
    for c in range(0, 5):
        matriz[l][c] = int(input(f'Digite o valor de {l},{c}: '))
for l in range(0, 5):
    for c in range(0, 5):
        print(f'{matriz[l][c]:>5}',end=" ")
    print()