fibo0 = 0
fibo1 = 0
v1 = list()
for c in range(0, 20):
    print(c)
    fibo1 = fibo1 + fibo0
    fibo0 = fibo1 - fibo0
    v1.append(fibo1)
    if fibo1 == 0:
        fibo1 = fibo1 + 1
print(v1)