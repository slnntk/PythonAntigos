import random
r1 = random.randint(0, 10)
tot = 0
print(r1)
print('A maquina ja fez a sua escolha, agora é sua vez de tentar acertar.')
num = int(input(f'Escolha aqui seu numero e faça sua (1º tentativa): '))

while num != r1:
    tot = tot + 1
    num = int(input(f'Escolha aqui seu numero e faça sua ({tot+1}ª tentativa): '))

print(f'Parabens você acertou de {tot+1}ª')
