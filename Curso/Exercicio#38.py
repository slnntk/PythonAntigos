n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    maior = n1
    print(f'\033[1;033m O numero {n1} é maior que o numero {n2}\033[m')
elif n2 > n1:
    maior = n2
    print(f'\033[1:032m O numero {n2} é maior que o numero {n1}\033[m')
else:
    print(f'\033[0:031m Os numeros são iguais então nao existe um maior que o outro!\033[m')