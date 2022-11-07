matriz = dict()
lista = list()
c = 1
maior = menor = 0
nomemaior = nomemenor = ""
while c < 5:
    print(f'{c}ª funcionario.')
    matriz["Matricula"] = str(input('Matricula: '))
    matriz["Nome"] = str(input('Nome: '))
    matriz["Função"] = str(input('Função: '))
    matriz["Salario"] = float(input('Salario: '))
    lista.append(matriz.copy())
    print()
    c = c + 1
p = 0
for k, v in enumerate(lista):
    if p == 0:
        maior = v['Salario']
        menor = v['Salario']
        nomemaior = v['Nome']
        nomemenor = v['Nome']
    else:
        if v['Salario'] > maior:
            maior = v['Salario']
            nomemaior = v['Nome']
        if v['Salario'] < menor:
            menor = v['Salario']
            nomemenor = v['Nome']
    p += 1
print(f'O que detém o maior salario é o {nomemaior} com R$: {maior}')
print(f'O que detém o menor salario é o {nomemenor} com R$: {menor}')



