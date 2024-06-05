"""Дано целое число N (>0). 
Вывести наибольшее из целых чисел К, 
для которых сумма 1 + 2 + … + К будет 
больше или равна N, и саму эту сумму."""

k = 0 # Инициализация
sumn = 0

while True: # Начало бесконечного цикла до получения нужного ввода
    try:
        n = input("Введите число n: ") # Ввод строки от пользователя.
        if int(n) >= 0: n = int(n) # Попытка преобразовать введенную строку в нужный формат.
        else: raise ValueError() #Ошибка если n < 0
        while sumn < n:
            k += 1
            sumn += k
        print(f"Наибльшее число при сложении последовательных чисел до {n} - {k}, а сумма - {sumn}")#Вывод ответа
        break
    except ValueError:
        print("Ошибка: было получено не число, не удалось преобразовать или n < 0") # Вывод сообщения об ошибке, если преобразование не удалось.
        continue