import os


my_path = r"C:\Users\Alexander Do\Documents\book1-exercises-master\book1-exercises-master\chp09\practice_files\little pics"

for current_folder, subfolders, file_names in os.walk(my_path):
	for file_name in file_names:
		full_path = os.path.join(current_folder, file_name)
		## Check if file is a JPG
		check_jpg = full_path.lower().endswith(".jpg")
		## CHeck if file is less than 2kb
		check_kb = os.path.getsize(full_path) < 2000
		if check_jpg and check_kb:
			print("Deleting {}.....".format(full_path))
			os.remove(full_path)