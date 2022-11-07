g = int(input('Numero de pessoas do grupo pesquisado: '))
print(f'Seu grupo terá {g} pessoas.\nComeçando......')
somai = 0
mediai = 0
nomemaisvelho = 0
idademaisvelho = 0
tot = 0

for c in range(1, g+1):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    somai = somai + idade
    if c == 1 and sexo in 'Mm':
        nomemaisvelho = nome
        idademaisvelho = idade
    if idade > idademaisvelho and sexo in 'Mm':
        nomemaisvelho = nome
        idademaisvelho = idade
    if sexo in 'Ff' and idade < 20:
        tot = tot + 1
mediai = somai / g
print(f'A media das idades nesse grupo de {g} pessoas é de {mediai} anos')
print(f'O homem mais velho é o {nomemaisvelho} e tem {idademaisvelho}')
print(f'Existem um total de {tot} mulheres com menos de 20 anos.')
