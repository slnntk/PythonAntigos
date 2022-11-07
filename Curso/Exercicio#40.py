n1 = int(input('Digite a sua primeira nota: '))
n2 = int(input('Digite a sua segunda nota: '))

m = (n1 + n2)/2

if m < 5:
    print(f'\033[1;33mSua media foi de {m} e você está \033[m\033[1:31mREPROVADO\033[m')
elif m < 6.9:
    print(f'\033[1;33mSua media foi de {m} e você está de \033[m\033[1:36mRECUPERAÇÃO\033[m')
else:
    print(f'\033[1;33mSua media foi de {m} e você está \033[m\033[1:34mAPROVADO\033[m')