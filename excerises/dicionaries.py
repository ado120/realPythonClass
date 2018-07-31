birthdays = {'Luke Skywalker': '5/24/19', 'Obi-Wan Kenobi': '3/11/57', 'Darth Vader': '4/1/41'}

if 'Yoda' not in birthdays:
	birthdays['Yoda'] = "unknown"

if 'Darth Vader' not in birthdays:
	birthdays['Darth Vader'] = "unkown"

for birthday in birthdays:
	print(birthday, birthdays[birthday])

del(birthdays['Darth Vader'])
print(birthdays)

birthdays = dict([("Luke Skywalker", "5/24/19"), ("Obi-Wan Kenobi", "3/11/57")])
print(birthdays)