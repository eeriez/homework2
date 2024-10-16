import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))

cursor.execute('SELECT COUNT(*) FROM Users')
num_of_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]

print(avg_balance)

connection.commit()
connection.close()
