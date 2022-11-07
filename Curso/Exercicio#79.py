lista = list()
while True:
    numero = int(input('Digite aqui um valor: '))
    if numero not in lista:
        lista.append(numero)
        operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
        if operador not in "SN":
            operador = str(input(f'Operação invalida, tente novamente [S/N]: ')).upper().strip()[0]
        if operador in "N":
            break
    else:
        print(f'O número que foi digitado é invalido, tente novamente: ')
print(f'A sua lista de valores em ordem crescente é  {sorted(lista)}')