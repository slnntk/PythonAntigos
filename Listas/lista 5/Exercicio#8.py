from random import randint
repetido = 0
inedito = 0
v1 = list()
v2 = list()
n = 0
for c in range(0, 10):
    n = randint(1, 10)
    if n not in v1:
        inedito += 1
    if n in v1:
        repetido += 1
        v2.append(n)
    v1.append(n)
print(v1)
print(v2)
