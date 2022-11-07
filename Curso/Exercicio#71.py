print('-*' * 30)
print('{:^30}'.format('Banco dos Esquisitolinos'))
print('-*' * 30)
valor = int(input('Valor do saque em R$: '))
tot = valor
ced = 200
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        print(f'Você pegou um {totced} cedulas de {ced}R$')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if tot == 0:
            break
















































'''print('-*' * 30)
print('{:^30}'.format('Banco dos Esquisitolinos'))
print('-*' * 30)
valor = int(input('Digite aqui o valor a ser sacado em R$: '))
tot = valor
ced = 200
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        print(f'Um total de {totced} de {ced}R$')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break'''
