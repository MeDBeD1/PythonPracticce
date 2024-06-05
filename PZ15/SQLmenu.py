#Написать БД учёта товаров на складе, таблица Товарный запас должна содержать –
#код товара, торговая марка, тип, цена, кол-во на складе, минимальный запас

import sqlite3
import add
import brandsearch
import codesearch
import minchange
import minsearch
import pricechange
import quantitychange
import output
import deletecode

# Соединяемся с БД
conn = sqlite3.connect('товарный_запас.db')
c = conn.cursor()

# Создаем таблицу "Товары"
c.execute('''
    CREATE TABLE IF NOT EXISTS Stock (
        code INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        stype TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        minquantity INTEGER NOT NULL
    )
''')

def find(c):
    print('Выберите действие:')
    print('1. Поиск по марке')
    print('2. Поиск по минимальному кол-ву')
    print('3. Поиск по коду')
    print('4. Вернуться')
    choice = int(input('Введите номер действия: '))


    if choice == 1:
        brandsearch.brandsearch(c)
    elif choice == 2:
        minsearch.minsearch(c)
    elif choice == 3:
        codesearch.codesearch(c)
    elif choice == 4:
        return
    else:
        print('Неверный номер действия')

def change(c):
    print('Выберите действие:')
    print('1. Изменить цену')
    print('2. Измененить минимальное кол-во товаров')
    print('3. Изменить кол-во на складе')
    print('4. Вернуться')
    choice = int(input('Введите номер действия: '))

    if choice == 1:
        pricechange.pricechange(c)
    elif choice == 2:
        minchange.quantitychange(c)
    elif choice == 3:
        quantitychange.quantitychange(c)
    elif choice == 4:
        return
    else:
        print('Неверный номер действия')



while True:
    print('Выберите действие:')
    print('1. Добавить товар')
    print('2. Найти товары')
    print('3. Редактировать товары')
    print('4. Удалить товары')
    print('5. Вывести БД')
    print('6. Выйти из программы')
    choice = int(input('Введите номер действия: '))

    if choice == 1:
        add.inputdata(c)
    elif choice == 2:
        find(c)
    elif choice == 3:
        change(c)
    elif choice == 4:
        print('Введите код товара на удаление')
        code = input()
        deletecode.delete_entry(c,code)
    elif choice == 5:
        output.output(c)
    elif choice == 6:
        break
    else:
        print('Неверный номер действия')

# Закрываем соединение с БД
conn.commit()
conn.close()
