import os 

my_path = r"C:\Users\Alexander Do\Documents\book1-exercises-master\book1-exercises-master\chp09\practice_files\images"

# get a list of all files and folders
file_names_list = os.listdir(my_path)

# loop over every file in the main folder
for file_name in file_names_list:
	if file_name.lower().endswith(".gif"): # extension matching a GIF file
		print("Converting {} to jpg.. ".format(file_name))
		#get full path and change the ".gif" to ".jpg"
		full_file_name = os.path.join(my_path, file_name)
		new_file_name = full_file_name[0:len(full_file_name) - 4] + ".jpg"
		os.rename(full_file_name, new_file_name)