while True:
	password = input("Enter password: ")
	if password == 'q' or password == 'Q':
		break
for i in range(1, 51):
	if (i % 3 == 0):
		continue
	print(i)