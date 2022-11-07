n1 = int(input('Digite aqui seu primeiro numero: '))
n2 = int(input('Digite aqui o seu segundo numero: '))
if n1 > n2 :
    maior = n1
    menor = n2
elif n2 > n1:
    maior = n2
    menor = n1
s = n1 + n2 #A soma dos dois numeros
m = n1 * n2 #Multplicação dos dois numeros
d = n1 / n2 #Divisao dos dois numeros
di = n1 // n2  #Divisao inteira dos dois numeros
e = n1 ** n2 #Exponencial entre n1 e n2
subtracao = maior - menor
divisaosimples = maior / menor

print(f'A soma é : {s}\nO produto é : {m}\nA divisão é {d} :')
print(f'Divisão inteira é: {di}\nA potencia é : {e}')
print(f'Subtração é : {subtracao}')









