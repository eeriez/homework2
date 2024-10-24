import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')

# for i in range(10):
#    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
#    (f'product{i + 1}', f'desc{i + 1}', f'{100 * (i + 1)}'))


def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    return products


connection.commit()
