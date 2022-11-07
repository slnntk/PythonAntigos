jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o jogador {jogador["Nome"]} jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'     Quantos gols {jogador["Nome"]} fez na partida {c+1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(jogador['Gols'])
    time.append(jogador.copy())
    operador = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if operador not in "SN":
        print("Erro!, digite apenas [S/N]")
        operador = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if operador in "N":
        break
print(f'{"COD":>3}{"Nome":>15}{"Gols":>15}{"Total":>15}')
for k, v in enumerate(time):
    print(f'{k:>2}', end='')
    for q in v.values():
        print(f'{str(q):>15}', end="")
    print()
print()
for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i+1} o jogador {jogador["Nome"]} fez um total de {v} gols')
    print(f'O total de gols foi de {jogador["Total"]}')


