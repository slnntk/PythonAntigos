num = [[], []]
valor = 0
par = list()
impar = list()
for c in range(1, 8):
    valor = int(input('Digite o valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
print(f'Todos os valores: {num}')
print(f'Os valores pares são: ', end=" ")
for v in num[0]:
    par.append(v)
    print(f'{sorted(v)}', end=" ")
print(f'\nOs valores impares são: ',end=" ")
for v in num[1]:
    impar.append(v)
    print(f'{sorted(v)}', end=" ")
