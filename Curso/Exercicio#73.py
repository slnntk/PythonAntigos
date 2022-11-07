tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza',
          'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Ceará',
          'Santos', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
          'Bahia', 'Juventude', 'Grêmio', 'Sport Recife', 'Chapecoense')
c = i = 0
k = 17
t = p = 1
operacao = " "
print('''Escolha qual a informação desejada:'
      Digite:
      1 - PRIMEIROS 5 COLOCADOS!
      2 - ÚLTIMOS 4 COLOCADOS !
      3 - LISTA DO TIME EM ORDEM ALFABÉTICA! 
      4 - POSIÇÃO DA CHAPECOENSE!
      5 - TABELA COMPLETA EM ORDEM.
      0 - FINALIZAR PROGRAMA. ''')
while True:
    operacao = " "
    if operacao not in (0, 1, 2, 3, 4, 5):
            operacao = int(input('\nDigite a operação desejada: '))
    if operacao == 0:
        break
    else:
        if operacao == 1:
            print(f'Os 5 primeiros colocados são os times: ')
            while t < 6 :
                for c in tabela[0:5]:
                    print(t, c)
                    t = t + 1
        if operacao == 2:
            print(f'Os últimos 4 colocados são os times: ')
            while k < 21:
                for c in tabela[(len(tabela)-4):(len(tabela))]:
                    print(k, c)
                    k = k + 1
        if operacao == 3:
            print(f'A lista do time em ordem alfabética é :')
            while p < 21:
                for c in sorted(tabela):
                    print(p, c)
                    p = p + 1
        if operacao == 4:
            print(f'A Chapecoense se encontra na posição de numero : {tabela.index("Chapecoense")+1}')
        if operacao == 5:
            print(f'A tabela completa em ordem: \n')
            while not i == 20:
                for l in tabela:
                    print(i+1, l)
                    i = i + 1
print(f'Programa finalizado.')





