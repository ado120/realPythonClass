import os

my_path = "C:/Users/Alexander Do/Documents/book1-exercises-master/book1-exercises-master/chp09/practice_files"

input_file_name = os.path.join(my_path, "example.txt")

with open(input_file_name, "r") as my_input_file:
	for line in my_input_file.readlines():
		print(line)