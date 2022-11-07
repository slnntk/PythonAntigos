import pyautogui,time

while True:
    pyautogui.click(100, 100)
    time.sleep(0.5)




'''somai = 0
mediai = 0
idadevelho = 0
nomevelho = 0

for c in range(1, 3):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    somai = idade + somai
    if c == 1 and sexo == 'M':
        idadevelho = idade
        nomevelho = nome
    if idade > idadevelho and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome


mediai = somai / 4
print(f'A media das idades é de : {mediai}')
print(f'A idade do homem mais velho é de {idadevelho} anos e seu nome é {nomevelho}')

------------------------------------------------------

somai = 0
mediai = 0
maisvelho = 0
nomemaisvelho = 0
tot = 0
for c in range(1, 4):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somai = idade + somai
    if sexo in 'Mm' and c == 1:
        maisvelho = idade
        nomemaisvelho = nome
    if idade > maisvelho and sexo in 'Mm':
         nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        tot = tot + 1
if nomemaisvelho == 0:
    print('Não há homens no grupo')


mediai = somai / 4
print(f'A media das idades do grupo é de {mediai}')
print(f'O homem mais velho do grupo é o {nomemaisvelho}')
print(f'Exitem um total de {tot} mulheres com menos de 20 anos no grupo.')

