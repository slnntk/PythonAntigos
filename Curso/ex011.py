ano = int(input('\033[4;037mDigite aqui o ano escolhido\033[m: '))

if ano % 4 == 0:
    print(f'\033[1;032mO ano de {ano} é bissexto!\033[m')
else:
    print(f'\033[1;031mO ano de {ano} não é bissexto!\033[m')
    print(f'\033[1;031mO ano de {ano} é \033[1;30m bissexto\033[m')
