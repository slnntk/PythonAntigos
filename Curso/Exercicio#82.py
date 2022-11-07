lista = list()
par = list()
impar = list()
operador = " "
while True:
    lista.append(int(input('Digite aqui um número: ')))
    operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if operador not in "SN":
        operador = str(f'Operação invalida digite apenas [S/N]: ').upper().strip()[0]
    for n in lista:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    if operador in "N":
        break
print(f'A lista completa tem os numeros: {lista} ')
print(f'A lista de números pares tem os números {par} ')
print(f'A lista de números impares tem os números {impar} ')


