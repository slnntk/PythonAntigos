n = int(input('Digite o numero de macas que voce quer comprar: '))

preco1 = n * 1.30
preco2 = n * 1

if n >= 12 :
    print(f'O valor das macas foi em atacado e teve desconto: {preco2}')
else :
    print(f'O valor das macas foi em varejo e nao teve desconto: {preco1}')


