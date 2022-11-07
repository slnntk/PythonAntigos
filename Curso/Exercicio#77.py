tupla = ('Mouse',
         'Teclado',
         'Monitor',
         'Processador',
         'Memoria',
         'Placa mae',)
for palavra in tupla:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
        