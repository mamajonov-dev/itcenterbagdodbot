import sqlite3


# def createtablequiz():
#     database = sqlite3.connect('database.sqlite')
#     cursor = database.cursor()
#     cursor.execute("""CREATE TABLE quizusers(
#     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name VARCHAR,
#     telefon VARCHAR,
#     age VARCHAR,
#     sana INTEGER,
#     chatid INTEGER
#     )""")
#     database.commit()
#     database.close()
#

# def createtableusers():
#     database = sqlite3.connect('database.sqlite')
#     cursor = database.cursor()
#     cursor.execute("""CREATE TABLE users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name VARCHAR,
#     chatid INTEGER UNIQUE
#     )""")
#     database.commit()
#     database.close()
#
#
# createtableusers()
#
