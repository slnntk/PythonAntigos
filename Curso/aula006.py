media = 0
for i in range(1, 4):

    salario = float(input(f'\n Digite o salario da {i} º pessoa:\n em (Reais)'))
    media = (salario + media)
    if i == 1:
        maior = salario
        menor = salario

if salario > maior:
    maior = salario
elif (salario < menor):
    menor = salario

print(f' O maior valor é {maior} e o menor e {menor}, e a media {media / (i)}')
