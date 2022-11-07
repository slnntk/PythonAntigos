totm = 0
toth = 0
for c in range(1,2):
    sexo = str(input('Digite aqui o seu sexo: ')).lower().strip()
    idade = int(input('Digite aqui a sua idade: '))
    anos = int(input('Digite aqui o numero de anos trabalhados: '))
    if sexo == 'homem' and idade >= 65 and anos >= 35:
        print(f'A aposentadoria do empregado {c} está valida.')
        toth = toth + 1
    elif sexo == 'mulher' and idade >= 60 and anos >= 30:
        print(f'A aposentadoria da empregada {c} está valida')
        totm = totm + 1
    else:
        print(f'A aposentadoria do empregado {c} está invalida')
print(f'Um total de {toth} empregados foram aposentaods\nUm total de {totm} empregados foram aposentaods')