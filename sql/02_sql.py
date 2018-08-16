import sqlite3

# create the new db if not created already
conn = sqlite3.connect("cars.db")

# create cursor object for SQL commands
cursor = conn.cursor()

# create the Table
cursor.execute("""CREATE TABLE inventory (Make TEXT, Model TEXT, Quanity INT)""")

conn.close()
