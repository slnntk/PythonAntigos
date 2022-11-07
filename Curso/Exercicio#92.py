from datetime import datetime
dados = dict()
salarioaposentadoria = 0
dados['Nome'] = str(input('Nome: ')).title().strip()
dados['Ano'] = int(input('Ano de nascimento: '))
idade = datetime.now().year - dados['Ano']
dados['CTPS'] = int(input('Carteira de trabalho: '))
if dados['CTPS'] != 0:
    dados['contratacao'] = int(input('Ano da contratação: '))
    dados['Salario'] = float(input('Salario:R$  '))
    dados['aposentadoria'] = idade + ((dados['contratacao'] + 35) - datetime.now().year)
if idade != 65:
    if datetime.now().year - dados['contratacao'] <= 20:
        salarioaposentadoria = 60 / 100 * (dados['Salario'] * 12 * (2021 - dados['contratacao']))
    else:
        salarioaposentadoria = (60 / 100 * ((dados['Salario'] * 2/100) * 12 * (2021 - dados['contratacao']))
for k, v in dados.items():
    print('-'*50)
    print(f'{k}: {v}')
print('-'*50)



