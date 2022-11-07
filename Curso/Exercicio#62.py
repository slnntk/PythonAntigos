a1 = int(input('Digite aqui um valor: '))
r = int(input('Digite aqui a razão: '))
t = a1
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{t} ->', end=" ")
        t = t + r
        c = c + 1
    print(t)
    mais = int(input('Quantos termos você quer mostrar a mais: '))

