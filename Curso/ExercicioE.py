ano = int(input('\033[4;037mDigite aqui o ano escolhido\033[m: '))

if ano % 4 == 0:
    print(f'\033[1;032mO ano de {ano} é bissexto!\033[m')
else:
    print(f'\033[1;031mO ano de {ano} não é bissexto!\033[m')

teste = list()
galera = list()
teste.append(str(input('Nome: ')).strip().title())
teste.append(int(input('Idade: ')))
galera.append(teste[:])
operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
while True:
    teste[0] = str(input('Nome: ')).strip().title()
    teste[1] = int(input('Idade: '))
    galera.append(teste[:])
    operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if operador not in "SN":
        operador = str(input('Escreva apenas [S/N]: ')).upper().strip()[0]
    if operador in "N":
        break
print(galera)