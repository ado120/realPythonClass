import os

my_path = r"C:\Users\Alexander Do\Documents\book1-exercises-master\book1-exercises-master\chp09\practice_files\images"

for current_folder, subfolders, files_names in os.walk(my_path):
	for file_name in files_names:
		print(os.path.join(current_folder, file_name))