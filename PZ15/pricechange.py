import sqlite3

def pricechange(c):
    code = int(input('Введите код товара для редактирования: '))
    newprice = float(input('Введите новую цену: '))

    c.execute('''
        UPDATE Stock
        SET price = ?
        WHERE code = ?
    ''', (newprice, code))
