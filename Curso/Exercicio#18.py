import math
a = float(input('Digite o angulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan((math.radians(a)))
print(f'O seno do angulo {a} é igual a: {sen}\nO cosseno do angulo {a} é igual a: {cos}\nA tangente do angulo {a} é igual a :{tan}')
print('============================================================================')
print(f'Para valores mais faceis para a conta ultilizamos:\nO seno do angulo {a} é igual a: {round(sen, 1)}\nO cosseno do angulo {a} é igual a: {round(cos, 1)}\nA tangente do angulo {a} é igual a: {round(tan, 1 )}')





