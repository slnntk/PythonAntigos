import random
n1 = random.randint(0, 5)
print(f'A maquina ja escolheu o numero, cabe a você acertar!')
num = int(input('Digite um numero de 0 a 5 e tente a sorte: '))

if num == n1 :
    print(f'Parabens o numero que você escolheu foi {num}, e você acertou!')
else:
    print(f'Você errou e o numero que a maquina escolheu foi {n1}')