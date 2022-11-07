c = int(input('Digite o valor do imóvel a ser adquirido: '))
s = int(input('Digite a sua renda mensal: '))
a = int(input('Em quantos anos você pretende pagar: '))

m = a * 12
p = c / m
c = s * m

if p <= (s * 0.30):
    print(f'\033[1;033mSeu emprestimo foi aceito, sua prestação irá ficar de {p}\nE você ira pagar em {m} meses \nO valor da casa que é de {c}')
else:
    print(f'\033[0:031mO valor excede sua condições e foi negado pelo banco!')


