"""Написать программу сформировывающая текстовый файл из последовательности целых положительных и отрицательных чисел. Файл должен быть следующим образом: 
Исходные данные 
Количество элементов
Индекс первого максимального элемента 
Произведение элементов средней трети
"""

import random as rng

def writeToFile(numberSequence):
    with open ('task1-1.txt', 'w') as file:
        file.write(f"{', '.join(map(str, numberSequence))}\n")

    with open('task1-2.txt', 'w') as file:
        # 1. Исходные данные
        file.write(f"Исходные данные:\n{', '.join(map(str, numberSequence))}\n")

        # 2. Количество элементов
        file.write(f"Количество элементов: {len(numberSequence)}\n")

        # 3. Индекс первого максимального элемента
        maxIndex = numberSequence.index(max(numberSequence))
        file.write(f"Индекс первого максимального элемента: {maxIndex}\n")

        # 4. Произведение элементов средней трети
        start = len(numberSequence) // 3
        end = 2 * start
        middleThird = numberSequence[start:end]
        product = 1
        for num in middleThird:
            product *= num
        file.write(f"Произведение элементов средней трети: {product}\n")


# Генерация случайной последовательности чисел
numberSequence = [rng.randint(-100, 100) for _ in range(10)]

# Вызов функции записи в файл
writeToFile(numberSequence)
