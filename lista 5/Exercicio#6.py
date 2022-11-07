import random
v1 = list()
for c in range(0, 10):
    v1.append(random.randint(1, 50))
print(v1)
n = int(input('Digite aqui o valor que deseja: '))
if n not in v1:
    print('Esse valor não está no vetor.')
if n in v1:
    print(f'Esse valor está no vetor v1 na posição {v1.index(n)}')