import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjascente: '))

hi = (co**2 + ca**2) / (1/2)
hi = math.hypot(co, ca)

print(f'O valor da hipotenusa, levando em conta que o cateto oposto é igual a {co} e o cateto adjascente é igual a {ca} é igual a: {math.hypot(co, ca)}')

