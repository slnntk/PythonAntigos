tupla = ('Mouse', 100,
         'Teclado', 300,
         'Monitor', 1200,
         'Processador', 800,
         'Memoria', 600,
         'Placa mãe', 500,)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end="R$ ")
    else:
        print(f'{tupla[pos]:>7.2f}')