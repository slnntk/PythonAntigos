import random
a = int(input('Digite o numero que você quer converter: '))
print(f'Digite 1 para\033[1;032m binario\033[m')
print(f'Digite 2 para\033[1;033m octal\033[m')
print(f'Digite 3 para\033[1;034m hexadecimal\033[m')
num = int(input('Qual é a base que você deseja escolher para converter o numero supracitado: '))

if num == 1:
    print(bin(a))
elif num == 2:
    print(oct(a))
elif num == 3:
    print(hex(a))
else:
    print(f'Não foi possivel identificar a operação')