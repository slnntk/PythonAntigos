'''def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9 ,1 ,0 , 2]
dobra(valores)
print(valores)'''
def soma(*valores):
    s = 0
    for núm in valores:
        s += núm
    print(f'Somando os valores temos {valores} temos {s}')


soma(5, 2)
soma(2, 9 ,4)



