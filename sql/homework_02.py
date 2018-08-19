import sqlite3


# open the connection
with sqlite3.connect('cars.db') as connection:
	c = connection.cursor()

	c.execute("UPDATE inventory SET quanity = 15 WHERE Model ='Mustang'")
	c.execute("UPDATE inventory SET quanity = 15 WHERE Model ='CRV'")

	print("\nNEW DATA:\n")

	rows = c.execute("SELECT * FROM inventory")

	for r in rows:
		print(r)

	print("\nFORD ROWS:\n")

	ford_rows = c.execute("SELECT * FROM inventory WHERE make = 'Ford'")

	for r in ford_rows:
		print(r)