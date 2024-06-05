import sqlite3

def minsearch(c):
    c.execute('''
        SELECT * FROM Stock
        WHERE quantity < minquantity
    ''')

    print('Результаты поиска:')
    for row in c:
        print(row)
