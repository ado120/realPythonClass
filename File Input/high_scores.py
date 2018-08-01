import csv
import os

my_path = "/Users/alexander/Documents/GIT/realPythonClass/book1-exercises-master/chp09/practice_files"

high_scores_dict = {}

with open(os.path.join(my_path, "scores.csv"), "r") as myFile:
	my_file_reader = csv.reader(myFile)
	for name, score in my_file_reader: #get each name/score pair
		score = int(score) #convert string score to int
		if name in high_scores_dict:
			if score > high_scores_dict[name]: # new score is higher
				high_scores_dict[name] = score
		high_scores_dict[name] = score

# for name in sorted(high_scores_dict):
# 	print name, high_scores_dict[name]

print(high_scores_dict)