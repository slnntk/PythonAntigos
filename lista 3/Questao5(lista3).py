primeiro = int(input('Primeira pessoa: '))
segundo  = int(input('Segunda pessoa : '))
terceiro = int(input('Terceira pessoa: '))
quarto = int(input('quarta pessoa: '))
quinto = int(input('quinta pessoa: '))
sexto = int(input('sexta pessoa: '))
setimo = int(input('setima pessoa: '))
oitavo = int(input('oitava pessoa: '))
nono = int(input('nona pessoa: '))
decimo = int(input('decima pessoa: '))

    # Achando a maior idade
maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro
if (quarto > maior):
        maior = quarto
if (quinto > maior):
        maior = quinto
if (sexto > maior):
        maior = sexto
if (setimo > maior):
        maior = setimo
if (oitavo > maior):
        maior = oitavo
if (nono > maior):
       maior = nono
if (decimo > maior):
        maior = decimo

print('Maior idade: ',maior)

    # Achando a menor idade
menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro
if (quarto < menor):
        menor = quarto
if (quinto < menor):
        menor = quinto
if (sexto < menor):
        menor = sexto
if (setimo < menor):
        menor = setimo
if (oitavo < menor):
        menor = oitavo
if (nono < menor):
        menor = nono
if (decimo < menor):
        menor = decimo

print('Menor idade: ',menor)
