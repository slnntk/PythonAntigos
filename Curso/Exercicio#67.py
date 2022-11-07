t = 0
while True:
    print(f'{"=" * 30}')
    n = int(input('Digite aqui o numero da tabuada desejada: '))
    print(f'{"="*30}')
    if n < 0:
        break
    t = t + 1
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print(f'O programa foi finalizado e você executou ele um total de {t}')
