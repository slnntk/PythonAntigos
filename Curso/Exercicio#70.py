tot = menorpreco = maiorpreco = c = produtomaior = 0
produtomenor = " "
while True:
    produto = str(input('Produto: '))
    preco = int(input('Preço: '))
    operador = " "
    c = c + preco
    while operador not in "SsNn":
        operador = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
        if preco > 1000:
            tot = tot + 1
        if c == 1:
            maiorpreco = preco
            produtomaior = produto
            tot = tot + preco
        if c == 1:
            menorpreco = preco
            produtomenor = produto
        else:
            if menorpreco > preco:
                menorpreco = preco
                produtomenor = produto
            if preco > maiorpreco:
                maiorpreco = preco
                produtomaior = produto
    if operador in "Nn":
        break
print(f'O produto mais barato é o {produtomenor} que custa {menorpreco}')
print(f'O produto mais caro é o {produtomaior} que custa {maiorpreco}')
print(f'Existem um total de {tot} produtos que custam mais de 1000 reais.')
print(f'O valor final de todas as compras é de {c}')






