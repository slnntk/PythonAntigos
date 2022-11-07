ci = cm = cmi = 0
while True:
    print('='*30)
    idade = int(input('Idade: '))
    sexo = " "
    while sexo not in "MmFf":
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        ci += 1
    if sexo in "Mm":
        cm += 1
    if sexo in "Ff" and idade < 20:
        cmi += 1
    operacao = " "
    while operacao not in "SsNn":
        operacao = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if operacao == "N":
        break

print(f'No cadastro há um total de {ci} pessoas maiores de 18 anos')
print(f'Foram cadastrados um total de {cm} homens.')
print(f'Dentre as pessoas cadastradas, a um total de {cmi} mulheres menores de 20 anos.')