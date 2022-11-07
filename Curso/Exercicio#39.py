ano = int(input('Digite aqui o ano de seu nascimento: '))
anos = 2021 - ano
if anos == 18 :
    print(f'\033[1:033mEstá na hora de se alistar, por que você tem {18} anos \033[m')
elif anos <= 17:
    print(f'\033[1:033mNão tenha pressa, você só tem {anos} anos e ainda não tá na hora de se alistar, ainda faltam {18 - anos} anos\033[m')
else:
    print(f'\033´1:031mVocê passou do periodo de alistamento, corra a junta militar mais proxima!\033[m')