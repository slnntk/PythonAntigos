frase = str(input('Digite aqui a sua frase: ')).strip().lower()
frase1 = frase.replace(" ", "")
fraseinvertida = frase1[::-1]

if frase1 == fraseinvertida:
    print(f'Essa frase {frase.capitalize()} é um palidrono!')
else:
    print(f'A frase {frase.capitalize()} não é um palidrono!')

