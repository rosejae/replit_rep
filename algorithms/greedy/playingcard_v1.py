import random

n, m = map(int, input().split())

matrix = [[random.randint(1, 9) for _ in range(m)] for _ in range(n)]
[print(f'{row}') for row in matrix]

print(max([min(row) for row in matrix]))