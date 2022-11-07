import random
for c in range(1,2):
    debito = random.randint(0,10000)
    print(f'O saldo da {c}ª pessoa é igual a: {debito}')
    credito = random.randint(0,10000)
    print(f'A pessoa {c}ª possui {credito} de credito')
    saque = int(input('Digite aqui o valor a ser sacado: '))
    if saque > debito:
        print(f'A pessoa  numero {c} não possui dinheiro suficiente para ser sacado: ')
    else:
        saque1 = debito - saque
        print(f'A pessoa  numero {c} fez um saque de {saque} e restou {saque1} real na sua conta.')
print(f'{c}: dinheiro na conta: {saque1} e credito de {credito}')