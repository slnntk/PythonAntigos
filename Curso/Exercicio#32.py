ano = int(input('Qual o ano que você quer descobrir: '))

if ano % 4 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto')

