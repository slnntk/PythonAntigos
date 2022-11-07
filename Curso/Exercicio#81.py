lista = list()
while True:
    n = int(input(f'Digite aqui o seu valor de numero : '))
    lista.append(n)
    operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if operador not in "SN":
        operador = str(input('Operação invalida digite apenas [S/N]: ')).upper().strip()[0]
    if operador in "N":
        break

print(f'\nForam digitados um total de {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não foi encontrado na lista.')
