ci = cm = cfi = 0
while True:
    print('='*30)
    idade = int(input('Idade: '))
    sexo = " "
    while sexo not in "MmFf":
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if sexo not in "MmFf":
            print(f'\n\033[0;031mSexo invalido, tente novamente.\033[m')
    if idade > 18:
        ci += 1
    if sexo in "Mm":
        cm += 1
    if sexo in "Ff" and idade < 20:
        cfi += 1
        operador = " "
        while operador not in "SsNn":
            operador = str(input('Você deseja continuar [S/N]: ')).upper().strip()[0]
            if operador not in "SsNN":
                print(f'\n\033[0;031mOperação invalida, tente novamente.\033[m')
        if operador in "Nn":
            break
print(f'No cadastro há um total de {ci} pessoas maiores de 18 anos')
print(f'Foram cadastrados um total de {cm} homens.')
print(f'Dentre as pessoas cadastradas, a um total de {cmi} mulheres menores de 20 anos.')
























































