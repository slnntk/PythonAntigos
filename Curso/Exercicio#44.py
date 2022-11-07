num = int(input('Digite o preço normal do produto: '))
print(f'Se você quer pagar a vista dinheiro/cheque e ter (10% de desconto) digite: 1')
print(f'Se você quer pagar a vista no cartão e ter (5% de desconto) digite: 2')
print(f'Se você quer pagar 2x no cartão e pagar o preço normal digite: 3')
print(f'Se você quer pagar 4x ou mais no cartão e pagar 20% de juros digite: 4')
operacao = int(input('Digite aqui como você vai pagar o produto: '))
print(f'Seu produto custa {num}')
if operacao == 1:
    num1 = num / 1.10
    print(f'O seu produto agora custa {num1} graças a operação 1')
elif operacao == 2:
    num2 = num / 1.05
    print(f'O seu produto agora custa {num2} graças a operação 2')
elif operacao == 3:
    num = num
    print(f'O seu produto não teve mudança de preço e custa {num}')
elif operacao == 4:
    num3 = num * 1.20
    print(f'O seu produto teve 20% de juros e agora custa {num3}')




