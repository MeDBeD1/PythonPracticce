import sqlite3

def codesearch(c):
    code = input('Введите код для поиска: ')

    c.execute('''
        SELECT * FROM Stock
        WHERE code = ?
    ''', (code))

    print('Результаты поиска:')
    for row in c:
        print(row)