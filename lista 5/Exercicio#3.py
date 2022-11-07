from random import randint
mult = 0
primos = list()
lista = list()
for c in range(1, 10):
    n = randint(1, 100)
    lista.append(n)
    for n in lista:
        if (n % n == 0):
            mult = mult + 1
        if (mult == 0):
            primos.append(n)
print(primos)
