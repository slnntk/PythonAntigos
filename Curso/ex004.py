d = dict()
lista = list()
a = int
maiorlen = 0
c = 0
while True:
    a = b = 0
    d['Nome'] = str(input('Nome do time! :  '))
    d['PG'] = int(input('Pontos ganhos :  '))
    d['GM'] = int(input('Gols marcados :  '))
    d['GS'] = int(input('Gols sofridos :  '))
    d['S'] = d['GM'] - d['GS']
    d['V'] = int(input('Numero de vitórias :  '))
    lista.append(d.copy())
    operador = str(input('Você quer continuar? [S/N]: ')).strip().lower()[0]
    if operador not in "sn":
        operador = str(input('Digite apenas: [S/N]: ')).strip().lower()[0]
    if operador in "n":
        break
    if d['GS'] != 0:
        ga = d['GM'] / d['GS']
    else:
        ga = d['GM']
for k, v in enumerate(lista):
    a = len(v['Nome'])
    b = a - 1
    print()
    for q in v.values():
        c = c + 1
        if c == 1:
            maiorlen = len(v['Nome'])
        else:
            if len(v['Nome']) > maiorlen:
                maiorlen = len(v["Nome"])
        if q == v["Nome"]:
            print(f'{v["Nome"]:.>{maiorlen}}', end= " ")
        else:
                print(f'{q:^{maiorlen}}', end=" ")
print(f'\n{"Nome":>{maiorlen}}{"PG":>{maiorlen-3}}{"GM":>{maiorlen-3}}{"GS":>{maiorlen-3}}{"SA":>{maiorlen-3}}{"VI":>{maiorlen-3}}')


