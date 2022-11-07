import random
n1 = str(input('O nome do primeiro aluno é: '))
n2 = str(input('O nome do segundo aluno é: '))
n3 = str(input('O nome do terceiro aluno é: '))
n4 = str(input('O nome do quarto aluno é: '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
