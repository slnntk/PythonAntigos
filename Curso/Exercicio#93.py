
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome: '))
tot = int(input(f'      Quantas partidas o jogador {jogador["Nome"]} jogou : '))
for c in range(0, tot):
    partidas.append(int(input(f'       Quantos gols {jogador["Nome"]} fez na partida {c+1}: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(jogador['Gols'])
for q, i in enumerate(jogador['Gols']):
    print(f'Na partida {q+1} o jogador {jogador["Nome"]} fez: {i} gols')
print(f'Fez um total de {jogador["Total"]} gols em {tot} jogos')