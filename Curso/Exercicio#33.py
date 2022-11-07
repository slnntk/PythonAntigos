n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = n1

if maior < n2:
    maior = n2
    if maior < n3:
        maior = n3
    print(f'O maior numero dentre os três numeros é o: {maior}')



