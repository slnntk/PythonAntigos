v1 = list()
pares = list()
for c in range(10, 20):
    v1.append(c)
    if c % 2 == 0:
        pares.append(c)
pares.sort()
print(pares)