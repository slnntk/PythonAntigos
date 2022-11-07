operacao = "S"
c = maior = menor = soma = media = 0

while operacao in "Ss":
    n1 = int(input("Digite um numero: "))
    soma = soma + n1
    c = c + 1
    operacao = str(input('Você quer continuar [S/N]: '))
    if c == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma / c
print(f'A media dentre os valores escritos é {media}')
print(f'O menor numero é o numero {menor} e o maior numero é o numero {maior}')
