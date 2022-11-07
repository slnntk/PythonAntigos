sexo = str(input(f'Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input(f'Sexo invalido digite [M/F]: ')).strip().upper()[0].strip().upper()[0]
print(f'Sexo aceito com sucesso! {sexo}')
