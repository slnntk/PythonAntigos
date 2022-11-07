frase = str(input('Digite aqui a sua frase: ')).lower().strip()
print(f'A letra "A" aparece um total de {frase.count("a")}')
print(f'A letra "A" aparece pela primeira vez na posição {frase.find("a")}')
print(f'A letra "A" aparece pela ultima vez na posição {frase.rfind("a")}')


