#В матрице найти максимальный элемент кратный 4

import random as rng

matrixSize = rng.randint(1,9), rng.randint(1,9)
matrix = [rng.choices(range(-99,99), k=matrixSize[0]) for _ in range(matrixSize[1])]

for row in matrix:
    print(row)

def max4numfunc(matrix):
    all4nums = (the4num for row in matrix for the4num in row if the4num % 4 == 0)
    return max(all4nums, default=None)

max4num = max4numfunc(matrix)

print(max4num)