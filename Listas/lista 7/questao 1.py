def soma():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print(a+b)
def subtracao():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print(a-b)
def divisao():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print(a/b)
def multiplicacao():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    print(a*b)

operador=1

while operador:
    print("""               0. Sair
               1. Somar
               2. Subtrair
               3. Multiplicação
               4. Divisão """)

    operador = int(input("Opção: "))

    if(operador==1):
        soma()
    if(operador==2):
        subtracao()
    if(operador==3):
        multiplicacao()
    if(operador==4):
        divisao()
