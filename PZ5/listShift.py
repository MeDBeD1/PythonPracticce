import random as rng

"""Описать функцию для выполнения 
циклического сдвига вправо"""

def shiftRight(lst):
    lst = lst[::-1] #Переворот массива
    lst.append(lst.pop(0)) #Добавляем к массиву первый его элемент в конец и удаляем его на 0й позиции
    lst = lst[::-1]
    return lst

lst = [rng.randint(0,99),rng.randint(0,99),rng.randint(0,99),rng.randint(0,99)] #Создание массива из случайных чисел
print(lst, "\n", shiftRight(lst), sep="") #Вывод изначального массива и преобразованого