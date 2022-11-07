g = int(input('Digite aqui quantas pessoas existem no seu grupo de pesquisa: '))
print(f'Seu grupo de pesquisa terá um total de {g} pessoas.\nComeçando o programa.....')
somai = 0
mediai = 0
idademaisvelho = 0
nomemaisvelho = 0
tot = 0

for c in range(1, g+1):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    somai = somai + idade
    if c == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade > idademaisvelho and sexo in 'Mm':
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        tot = tot + 1

mediai = somai / g
print(f'A media entre as idades do seu grupo de {g} pessoa é de: {mediai}')
print(f'A pessoa mais velha do grupo é o {nomemaisvelho} que possui {idademaisvelho} anos')
print(f'Existem um total de {tot} mulheres com menos de 20 anos.')


