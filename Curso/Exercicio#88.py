from random import randint
lista = list()
jogos = list()
tot = 1
cont = 0
quant = int(input('Digite a quantidade de jogos que você deseja: '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'SORTEANDO SEUS JOGOS')
for i, l in enumerate(jogos):
    print(f'JOGO {i+1} : {l}')