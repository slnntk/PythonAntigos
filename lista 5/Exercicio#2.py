v1 = list()
v2 = list()
v3 = list()
for c in range(2, 20):
    if c % 2 == 0:
        c = c * c
        v1.append(c)
for c in range(10, 19):
    v2.append(c)
v3 = v1 + v2
v3.sort()
print(v3)


