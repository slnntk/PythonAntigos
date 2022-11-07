algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'So tem espaços : {algo.isspace()} \n É um numero? : {algo.isnumeric()} \n É um alfanumerico? : {algo.isalnum()}')
print(f'È capitalizado? : {algo.istitle()} \n É maiscula? : {algo.isupper()} \n É um minuscula? : {algo.islower()}')


