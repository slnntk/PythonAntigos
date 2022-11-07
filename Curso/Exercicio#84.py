conjunto = list()
temporario = list()
mai = men = 0
while True:
    temporario.append(str(input('Nome: ')).title())
    temporario.append(int(input('Peso: ')))
    if len(conjunto) == 0:
        mai = men = temporario[1]
    else:
        if temporario[1] > mai:
            mai = temporario[1]
        if temporario[1] < men:
            men = temporario[1]
    conjunto.append(temporario[:])
    temporario.clear()
    operador = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if operador not in "SN":
        operador = str(input("Operação invalida escreva apenas [S/N]: ")).strip().upper()[0]
    if operador in "N":
        break
print(f'Foram cadastradas um total de {len(conjunto)} pessoas')
print(f'O maior peso foi de {mai} e pertence as ', end=" ")
for p in conjunto:
    if mai == p[1]:
        print(p[0], end=" ")
print(f'O menor peso foi de {men} e pertence as', end=" ")
for p in conjunto:
    if men == p[1]:
        print(p[0], end=" ")
