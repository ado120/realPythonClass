import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	# create a table called numbers and drop/delete if it already exists in the db
	c.execute("DROP TABLE if exists numbers")
	c.execute("CREATE TABLE numbers(num int)")

	for i in range(100):
		c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))