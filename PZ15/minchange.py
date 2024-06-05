import sqlite3

def quantitychange(c):
    code = int(input('Введите код товара для редактирования: '))
    newminquantity = int(input('Введите новое значение минимального запаса: '))

    c.execute('''
        UPDATE Stock
        SET minquantity = ?
        WHERE code = ?
    ''', (newminquantity, code))