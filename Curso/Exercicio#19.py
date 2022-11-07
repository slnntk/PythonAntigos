import random

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

r = random.randint(1, 4)
print(f'O numero escolhido foi: {r}')

if r == 1 :
    print(f'O numero corrresponde a: {aluno1}')
elif r == 2 :
    print(f'O numero corrresponde a: {aluno2}')
elif r == 3:
    print(f'O numero corrresponde a: {aluno3}')
elif r == 4:
    print(f'O numero corrresponde a: {aluno4}')

    aluno1 = 1
    aluno2 = 2
    aluno3 = 3
    aluno4 = 4






