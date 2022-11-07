ano = int(input('Digite o ano que você nasceu: '))
idade = 2021 - ano
if idade <= 9:
    print(f'Você se enquadra na categoria \033[1;034mMIRIM\033[m por possuir {idade} anos')
elif idade <= 14:
    print(f'Você se enquadra na categoria \033[1;033mINFANTIL\033[m por possuir {idade} anos')
elif idade <= 19:
    print(f'Você se enquadra na categoria \033[1;035mJUNIOR\033[m por possuir {idade} anos')
elif idade <= 19:
    print(f'Você se enquadra na categoria \033[1;036mSENIOR\033[m por possuir {idade} anos')
else:
    print(f'Você se enquadra na categoria \033[1;031mMASTER\033[m por possuir {idade} anos')


