n1 = int(input('Digite aqui o valor: '))
c = n1
f = 1

while c > 0:
    print(f'{c}', end=" ")
    print(' x ' if c > 1 else ' = ', end=" ")
    f = f * c
    c = c - 1
print(f)