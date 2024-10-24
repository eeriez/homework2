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

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')


def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    return products


def add_users(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    check = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check is None:
        return False
    else:
        return True


connection.commit()
