nome = str(input('Qual é seu nome: ')).strip().lower()
if 'tiago' in nome:
    print(f'Que nome bonito.')
elif 'livia' in nome:
    print(f'Nossa, é o nome da minha namorada!')
elif nome in 'pedro' or nome in 'maria' or nome in 'paulo':
    print('seu nome é bem comum aqui no brasil')
print(f'Bom dia {nome}')


