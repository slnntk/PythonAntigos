from time import sleep
print('Digite 1 para começar a contagem!: ')
a = int(input('SUA OPERAÇÃO: '))
if a == 1:
    for c in range(10, 0-1, -1):
        sleep(1)
        print(f'{c}')
        if c == 0:
            sleep(0.5)
            print('KABOOOOM')
else:
    print('A contagem so começara se a operação for a correta ')
