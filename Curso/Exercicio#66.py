n = c = s = 0
while n != 999 :
    n = int(input('Digite aqui o seu numero: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print(f'A soma entre os numeros digitados é de {s} e você digitou um total de {c} números.')