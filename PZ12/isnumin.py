#Проверить на наличие числа k внутри числа n

import random as rng

n = rng.randint(-9999,9999)
k = rng.randint(-999,999)

def check(n,k):
    n = abs(n)
    k = abs(k)

    if str(n).find(str(k)) != -1: print(f'{k} было найдено внутри {n}')
    else: print(f'{k} не было найдено внутри {n}')

check(n,k)