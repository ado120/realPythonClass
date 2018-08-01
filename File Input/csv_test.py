import csv
import os

my_path = "/Users/alexander/Documents/GIT/realPythonClass/book1-exercises-master/chp09/practice_files"

with open(os.path.join(my_path, "wonka.csv"), "r") as my_file:
	my_file_reader = csv.reader(my_file)
	next(my_file_reader)
	for row in my_file_reader:
		print(row)