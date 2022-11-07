from random import randint
v1 = list()
par = impar = 0
for c in range(0, 10):
    n = randint(1, 50)
    v1.append(n)
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'No vetor {v1}, existem {par} pares e {impar} impares ')