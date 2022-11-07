lista = list()
def escreva(lista):
    for k, v in enumerate(lista):
            print('-' * (len(v)+4))
            print(f'  {(v)}')
            print('-' * (len(v)+4))



print(f'Escreva suas mensagens')
a = str(input(': '))
b = str(input(': '))
c = str(input(': '))
escreva(lista = (a, b ,c))







