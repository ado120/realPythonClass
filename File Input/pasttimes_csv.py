import csv
import os

##NOT DONE

my_path = "/Users/alexander/Documents/GIT/realPythonClass/book1-exercises-master/chp09/practice_files"

with os.path.join(my_path, "pastimes.csv", "r") as my_file:
	my_file_reader = csv.reader(my_file)
	my_file_writer = csv.writer()
	next(my_file_reader)
	for row in my_file_reader:
		if row[1].lower().find("fighting") != 1:
			row.append("Combat")
		else:
			row.append("Other")