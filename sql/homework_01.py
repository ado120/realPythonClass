import sqlite3

# open up the database
with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	# insert the data into the inventory table
	c.execute("INSERT INTO inventory VALUES('Ford', 'Mustang', '10')")
	c.execute("INSERT INTO inventory VALUES('Ford', 'Focus', '10')")
	c.execute("INSERT INTO inventory VALUES('Ford', 'Ranger', '10')")
	c.execute("INSERT INTO inventory VALUES('Honda', 'Accord', '10')")
	c.execute("INSERT INTO inventory VALUES('Honda', 'CRV', '10')")