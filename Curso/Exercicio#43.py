
altura = int(input('Digite a sua altura: '))
peso = int(input('Digite o seu peso: '))

imc = peso / (altura ** 2)
p1 = (18.5 * (altura**2)) / 10000
p2 = (25 * (altura**2)) / 10000
print(f'Seu peso ideal minimo é igual a: {p1}')
print(f'Seu peso ideal maximo é igual a: {p2}')


if imc <= (18.5/10000):
    print(f'A pessoa está abaixo do peso e seu imc é {imc * 10000} ')
elif imc <= (25/10000):
    print(f'A pessoa está com peso ideal e seu imc é {imc * 10000} ')
elif imc <= (30/10000):
    print(f'A pessoa está com sobre peso e seu imc é {imc * 10000} ')
elif imc <= (40/10000):
    print(f'A pessoa está com Obesidade  e seu imc é {imc * 10000 } ')
else:
    print(f'A pessoa está com Obesidade mórbida e seu imc é {imc * 10000} ')

