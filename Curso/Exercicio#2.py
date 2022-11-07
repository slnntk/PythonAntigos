pessoas = dict()
lista = list()
mei = 0
mulheres = list()
velhos = list()
velhos1 = list()
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).title().strip()
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoas['Sexo'] not in "MF":
            print(f'Erro!, digite apenas [M/F]')
        else:
            break
    pessoas['Idade'] = int(input('Idade: '))
    mei += pessoas['Idade']
    lista.append(pessoas.copy())
    operador = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if operador not in "SN":
        print(f'Erro!, digite apenas [S/N]')
        operador = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if operador in "N":
        break
print(f'Foram cadastradas um total de {len(lista)} pessoas')
mei = mei / len(lista)
print(f'A média de idade do grupo é de {mei}')
for k, v in enumerate(lista):
    if v['Sexo'] == "F":
        mulheres.append(v['Nome'])
print(f'Tem um total de {len(mulheres)} cadastradas e são elas {mulheres}')
for k, v in enumerate(lista):
    if v['Idade'] > mei:
        velhos.append(v['Nome'])
        velhos.append(v['Idade'])
for k, v in enumerate(velhos):
    print(f'As pessoas que estão acima da media de idade são as {velhos}')









