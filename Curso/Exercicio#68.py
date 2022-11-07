import random
s = " "
n = 0
r1 = " "
while True:
    r = random.randint(1, 10)
    p = ["PAR", "IMPAR"]
    s = str(input('Digite aqui se você quer ser Par ou Impar: ')).strip().upper()
    if s == "PAR":
        r1 = "IMPAR"
    elif s == "IMPAR":
        r1 = "PAR"
    n = int(input('Digite aqui o seu número: '))
    if r1 == "PAR" and s == "IMPAR":
        if (r + n) % 2 == 0:
            print(f'A vitoria foi da máquina, por que ela escolheu {r}')
            break
        else:
            print(f'A vitoria foi sua por que a maquina escolheu o numero {r}')
    if r1 == "IMPAR" and s == "PAR":
        if (r + n) % 2 != 0:
            print(f'A vitoria foi da máquina, por que ela escolheu {r}')
            break
        else:
            print(f'A vitoria foi sua por que a maquina escolheu o numero {r}')







