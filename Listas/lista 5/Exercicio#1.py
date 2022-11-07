from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(n)
for r in n:
    print(r, end=" ")
print(f'\nO maior numero é o numero {max(n)}')
print(f'O menor numero é o numero {min(n)}')
print(f'Em ordem crescente é {sorted(n)}')
print(f'Em ordem crescente é {sorted(n, reverse=True)}')