import sqlite3

def inputdata(c):
    mark = input('Введите торговую марку: ')
    type = input('Введите тип: ')
    price = float(input('Введите цену: '))
    quantity = int(input('Введите количество на складе: '))
    minquantity = int(input('Введите минимальный запас: '))

    c.execute('''
        INSERT INTO Stock (brand, stype, price, quantity, minquantity)
        VALUES (?, ?, ?, ?, ?)
    ''', (mark, type, price, quantity, minquantity))
    code = c.lastrowid
    print(f'Успешно добавленно код: {code} марка: {mark} тип товара: {type} цена: {price} кол-во на складе: {quantity} минимально допустимое кол-во: {minquantity}')