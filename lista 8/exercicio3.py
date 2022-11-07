def main():
    n = int(input("Digite o valor do primeiro numero. : "))

    m = int(input("Digite o valor do segundo numero. : "))

    mdc = n
    while n % mdc != 0 or m % mdc != 0:
        mdc = mdc - 1

    print(f'{(n, m)} = {mdc}')

main()