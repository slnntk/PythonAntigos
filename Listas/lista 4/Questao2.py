h = int(input('Digite as horas trabalhadas: '))
s = int(input('Digite o preco da hora: '))

d = h * s
reajuste = (h - 40) + (s * 1.5)

if h <= 40:
    print(f'O seu salario é igual a : {d}')
else:
    print(f'Seu salario foi de {d} para {d + reajuste}')


