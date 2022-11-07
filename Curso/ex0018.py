galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 4):
    dado.append(str(input('Nome: ')).title())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade pois possui {p[1]} anos.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade e so vai ser maior de idade daqui a {18 - p[1]} anos')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')
--------------------------------------------------------------------------------------------------
galera = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')).title())
    dados.append(int(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    galera.append(dados[:])
    dados.clear()

    operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if operador not in "SN":
        operador = str(input('Operação invalida tente apenas [S/N]: ')).upper().strip()
    if operador in "N":
        break
print(f'Foram cadastradas um total de {len(galera)}')
print(f'O maior peso foi {mai}', end=" ")
for p in galera:
    if mai == p[1]:
        print(f'e pertence a {p[0]}')
print(f'O menor peso foi {men}', end=" ")
for p in galera:
    if men == p[1]:
        print(f'e pertence a {p[0]}')