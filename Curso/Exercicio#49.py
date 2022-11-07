i = int(input('Digite o incio: '))
f = int(input('Digite o final: '))
n = int(input('Numero desejado da tabuada: '))
for c in range(i, f+1):
    print(f'[{c}] * [{n}] = [{c * n}]')
