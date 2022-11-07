tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quartoze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O numero {num} por extenso é igual a: {tupla[num]}')
        operacao = str(input(f'Você quer parar? [S/N]: ')).upper().strip()[0]
        if operacao not in 'SsNn':
            print(f'Operação invalida!! ', end=" ")
            operacao = str(input(f'Você quer parar? [S/N]: ')).upper().strip()[0]
        if operacao in "Ss":
            break
        else:
            print(f'Você decidiu continuar.')
    else:
        print(f'Tente novamente', end=" ")
print(f'Programa finalizado.')