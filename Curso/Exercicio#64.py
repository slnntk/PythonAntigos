c = 0
n1 = int(input(f'Digite um numero: '))
soma = n1
while n1 != 999:
    n1 = int(input(f'Digite outro numero, você está na tentativa numero {c+1}: '))
    c = c + 1
    soma = soma + n1
print(f'Você usou um total de {c} tentativas e a soma dos numeros digitados é de {soma}')