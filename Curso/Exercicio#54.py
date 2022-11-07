from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for p in range(1, 5):

    nasc = int(input(f'\033[m{p}ª pessoa, Digite aqui a sua data de nascimento: '))
    idade = atual - nasc
    if idade < 18:
        totmenor = totmenor + 1
        print('\033[1:036m')
        print(f'\033[1:033mA pessoa {p} é menor de idade e possui {idade} anos.')
    else:
        print('\033[1:031m')
        print(f'\033[1:032mA pessoa {p} é maior de idade e possui {idade} anos. ')
        totmaior = totmaior + 1
print(f'Existem um total de {totmenor} pessoas menor de idade\nE um total de {totmaior} pessoa maior de idade!')