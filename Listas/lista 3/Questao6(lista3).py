def sum(a, b, c):
    return (a + b + c)

for mediaaluno in range(1, 10):
     
    
    a = float(input('Digite 1 nota: '))
    b = float(input('Digite 2 nota: '))
    c = float(input('Digite a 3 nota: '))


media1 = (a + b + c ) 
mediaaluno = (a + b + c ) / 3 
mediageral = media1 / 10 

print(mediaaluno)

if(mediaaluno) >= 7:
   print("Aprovado")

if(mediaaluno) <= 7:
   print("AF") 
   
if(mediaaluno) <= 4:
   print("Reprovado")
   print(mediaaluno)
print(mediageral)
