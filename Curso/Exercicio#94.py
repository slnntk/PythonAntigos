lista = list()
pessoas = dict()
tot = 0
mediaidade = 0
mulheres = list()
velhos = list()
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).title()
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['Sexo'] not in "MF":
            print(f'Erro!, digite o sexo corretamente [M/F]')
        else:
            break
    pessoas['Idade'] = int(input('Idade: '))
    mediaidade += pessoas['Idade']
    lista.append(pessoas.copy())
    operador = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
    if operador not in "SN":
        print(f'Erro!, digite a operação corretamente [S/N]')
        operador = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
    if operador in "N":
        break
mediaidade = mediaidade / len(lista)
print(f'Um total de {len(lista)} pessoas foram cadastradas com sucesso.')
print(f'A media da idade foi {mediaidade}')
for k, v in enumerate(lista):
    if v['Sexo'] == "F":
        mulheres.append(v['Nome'])
print(f'Foram cadastradas um total de {len(mulheres)} mulheres e são elas {mulheres}')
for k, v in enumerate(lista):
    if v['Idade'] > mediaidade:
        velhos.append(v['Nome'])
        velhos.append(v['Idade'])
print(f'As pessoas que estão acima da media de idade são as {velhos}')
print(lista)

