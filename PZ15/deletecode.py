import sqlite3

conn = sqlite3.connect('товарный_запас.db')

def delete_entry(c, code):
    c.execute("DELETE from Stock WHERE code=?", (code,))
    conn.commit()
    print("Успешно удалено")
