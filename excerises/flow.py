word = input("Please enter a word: ")

if len(word) == 5:
	print("Input is 5 characters")
elif len(word) < 5:
	print("Input is less than 5 characters")
else:
	print("Input is greater than 5 characters")