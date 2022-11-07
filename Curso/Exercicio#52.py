n = int(input('Digite o numero que você deseja descobrir: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot = tot + 1
        print('\033[1;033m', end=" ")
    else:
        print('\033[0;031m', end=" ")
    print(c, end=" ")
print(f'\n\033[mO numero {n} tem um total de divisores de {tot}')
if tot == 2:
    print(f'O numero {n} é primo!')
else:
    print(f'O numero {n} não é primo!')