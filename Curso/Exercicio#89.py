ficha = list()
while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if operador not in "SN":
        operador = str(input('Digite apenas [S/N]: ')).upper().strip()[0]
    if operador in "N":
        break
print(f'-'*30)
for i, a in enumerate(ficha):
    print(f'{i}  {a[0]}  {a[1]}  {a[2]}')
print(f'-'*30)

