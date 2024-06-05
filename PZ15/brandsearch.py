import sqlite3

def brandsearch(c):
    mark = input('Введите торговую марку для поиска: ')

    c.execute('''
        SELECT * FROM Stock
        WHERE brand = ?
    ''', (mark,))

    print('Результаты поиска:')
    for row in c:
        print(row)