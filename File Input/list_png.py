import glob
import os

my_path = r"C:\Users\Alexander Do\Documents\book1-exercises-master\book1-exercises-master\chp09\practice_files\images"
possible_files = os.path.join(my_path, "*/*.png")

for file_name in glob.glob(possible_files):
	print(file_name)