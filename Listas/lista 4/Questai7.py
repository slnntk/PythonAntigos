csalario = 0
cfilhos = 0
cmenor = 0
c1 = 0
j = int(input('Digite o numero de pessoas pesquisadas!'))
for c in range(1, j+1):
    salario = int(input(f'Digite o valor do salario da pessoa {c}: '))
    filhos = int(input(f'Digite quantos filhos a pessoa {c} tem: '))
    csalario = salario + csalario
    if filhos > 0:
        cfilhos = filhos + cfilhos
    if salario < 1000:
            c1 += 1
mediasala = csalario / j
print(f'A media salarial da cidade é de: {mediasala}')
print(f'A media na quantidade de filhos da cidade é de: {cfilhos}')
print(f'O percentual de pessoas com salario menor que 1000 é de : {c1 / (j/100)}%')
