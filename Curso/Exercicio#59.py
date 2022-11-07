n1 = int(input(f'\n\033[1;033mDigite aqui o seu primeiro valor: '))
n2 = int(input(f'\nDigite aqui o seu primeiro valor: \033[m'))
operacao = 0
maior = 0
while operacao != 5:
    print('''\n\033[1;036m             [1] SOMA
             [2] MULTIPLICAÇÃO
             [3] MAIOR NUMERO
             [4] NOVOS NÚMEROS
             [5] FECHAR PROGRAMA                        
                                 \033[m''')
    operacao = int(input('Digite aqui qual a operação que voce quer: '))
    if operacao == 1:
        print(f'\nA soma entre os valores de {n1} e {n2} é igual a {n1+n2}')
    elif operacao == 2:
        print(f'\nA multiplicação entre os valores de {n1} e {n2} é igual a {n1*n2}')
    elif operacao == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        print(f'\nO maior numero dentre os números {n1} e {n2} é igual a {maior}')
    elif operacao == 4:
        n1 = int(input(f'\n\033[1;033mDigite aqui o seu primeiro valor: '))
        n2 = int(input(f'\nDigite aqui o seu primeiro valor: \033[m'))

print('\n\033[031mPrograma finalizado!')
