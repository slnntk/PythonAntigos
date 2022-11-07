s = int(input('Digite o valor do seu salario: '))

n1 = s

if s >= 1250:
    s = s * 1.10
else:
    s = s * 1.15

print(f'Seu salario foi de {n1} para {s}')