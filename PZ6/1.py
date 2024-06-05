import random as rng

#Вывести массив сначала с нечётными индексами, потом с чётными

listA = rng.sample(range(0,100), rng.randint(0,10))

print(f"Начальный массив:{listA}")

print(f"Модифицированный массив {listA[::2]+listA[1::2]}")

