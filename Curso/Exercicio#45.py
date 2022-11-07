import random

print(f't = tesoura')
print(f'p = papel')
print(f'd = pedra')
a = str(input('Digite o que você escolheu: ')).strip().lower()
lista = ['t', 'd', 'p']
b = random.choice(lista)
print(b)

if b == 'd' and a == 't':
    print('A maquina ganhou e você perdeu!')
elif b == 'd' and a == 'p':
    print('Você ganhou e a maquina perdeu!')
elif b == 'd' and a == 'd':
    print('Você empatou com a maquina!')
elif b == 't' and a == 't':
    print('Você empatou com a maquina!')
elif b == 't' and a == 'p':
    print('A maquina ganhou e você perdeu!')
elif b == 't' and a == 'd':
    print('A maquina perdeu e você ganhou')
elif b == 'p' and a == 't':
    print('Você ganhou e a maquina perdeu!')
elif b == 'p' and a == 'p':
    print('Você empatou com a maquina!')
elif b == 'p' and a == 'd':
    print('Você perdeu e a maquina ganhou!')





