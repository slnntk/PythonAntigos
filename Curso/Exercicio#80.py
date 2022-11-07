lista = list()
for q in range(0, 5):
    n = int(input('Digite aqui um valor: '))
    if q == 0:
        lista.append(n)
    elif n > len(lista)-1:
        lista.append(n)

    else:
        if n > n:
            lista.insert(n, q+1)
        else:
            lista.append(n)
print(lista)