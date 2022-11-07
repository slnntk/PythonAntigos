num = int(input('Digite um numero: '))
count = 0
for c in range(1, num + 1):
    if num % c == 0:        
        count = count + 1
    else:            
         print('{} '.format(c), end='')
if count == 2:
      print('Primo')
else : 
      print('Nao primo')
 
