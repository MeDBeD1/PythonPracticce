#Для каждой строки матрицы с нечётным номером, найти среднее арифметическое её элементов

import random as rng

matrixSize = rng.randint(1, 9), rng.randint(1, 9)
meanList = []

matrix = [[rng.randint(-2, 2) for _ in range(matrixSize[0])] for _ in range(matrixSize[1])]

meanList = [sum(row) / len(row) if index % 2 != 0 else None for index, row in enumerate(matrix, start=1)]

for row in matrix:
    print(row)

print(meanList)
