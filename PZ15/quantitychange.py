import sqlite3

def quantitychange(c):
    code = int(input('Введите код товара для редактирования: '))
    newquantity = int(input('Введите новое количество на складе: '))

    c.execute('''
        UPDATE Stock
        SET quantity = ?
        WHERE code = ?
    ''', (newquantity, code))