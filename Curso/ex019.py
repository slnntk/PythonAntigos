#keys são as informações         (nome, sexo, idade)
#values são os valores das keys  (Cássio, M,     19)
#items é o conjunto de itens do dicionario ('nome': 'Cássio', 'sexo': 'M', 'idade': 19)

pessoas = {'nome': 'Cássio', 'sexo': 'M', 'idade': 19}
pessoas['nome'] = 'Livia'
pessoas['sexo'] = 'F'
pessoas['peso'] = 68.5
for k, v in pessoas.items():
    print(f'{k} : {v}')

