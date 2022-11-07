def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)



def menu():
    n = int(input(f'Digite o numero de termos: '))

    for c in range(1, n+1):
        print(f'{fibo(c)}', end=", ")

while True:
    menu()










