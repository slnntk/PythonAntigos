tupla = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')),
         int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu um total de {tupla.count(9)}')
if 3 in tupla:
    print(f'Em que posição o número 3 foi encontrado {tupla.index(3)+1}')
else:
    print(f'Não existe nenhum número 3 na tupla.')
print(f'Os valores pares são os : ')
for r in tupla:
    if r % 2 == 0:
        print(f'{r}', end=" ")
