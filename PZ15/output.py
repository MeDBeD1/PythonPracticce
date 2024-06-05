import sqlite3

def output(c):
    c.execute('''
        SELECT * FROM Stock
    ''')

    print('Содержимое таблицы "Товары":')
    for row in c:
        print(row)