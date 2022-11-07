media = 0
quantidade = 10
for i in range(1, quantidade + 1):
  salario = float(input('\n Digite o salario da {i} º pessoa:\n em (Reais)'))
  media += salario

  if i == 1 :
    maior = salario
    menor = salario
  if salario > maior :
    maior = salario 
  elif (salario < menor) :
    menor = salario

  if (salario < 1500) :
    print(f' O funcionario {i} e INSENTO e tem {salario} ')
  elif (salario <= 2000) :
    salario = salario - (salario * 0.1)
    print(f' O funcionario {i} tem um desconto de 10% que fica : {salario}')
  elif (salario > 2000) :
    salario = salario - (salario * 0.15)
    print(f' O funcionario {i} tem um desconto de 15% que fica : {salario}')

print(f'O maior valor é { maior } e o menor e { menor }, e a media {media / quantidade }')
