i = int(input('Digite o o começo do intervalo: '))
f = int(input('Digite o final do intervalo: '))
p = int(input('Digite o valor do múltiplo que deseja achar: '))
s = 0
count = 0
for c in range(i, f+1, p-1):
    if c % 3 == 0:
        s = s + c
        count = count + 1
print(f'Entre o intervalo de {i} e {f} procuramos todos os {count} números impares múltiplos de {p}')
print(f'E a soma de todos eles é igual a {s} ')
