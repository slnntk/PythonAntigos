a1 = int(input('Digite aqui um valor: '))
r = int(input('Digite aqui a razão: '))
t = a1
c = 1

while c <= 10:
    print(f'{t} ->', end=" ")
    t = t + r
    c = c + 1
print(t)

