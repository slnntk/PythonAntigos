s = 0
i = int(input('Digite o numero inicial do intervalo: ')) #1
f = int(input('Digite o numero final do intervalo: ')) #6
for c in range(i, f+1):
    if c % 2 == 0:
        s = s + c
print(f'A soma dos números pares no intervalo de {i} a {f} é igual a {s}')
