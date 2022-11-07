a1 = int(input('Digite aqui o primeiro termo da p.a: '))
r = int(input('Digite aqui a razão da p.a: '))
an = a1 + ((10 - 1)*r)
for c in range(a1, an+1,r):
    print(c, end='-> ')
print('FIM')
print(f'Sua progressão aritmética que tem o primeiro termo {a1}\nRazão {r}, e tem 10 termos com seu enésimo termo {an}')