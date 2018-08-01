import os
import glob

my_path = r"C:\Users\Alexander Do\Documents\book1-exercises-master\book1-exercises-master\chp09\practice_files\images"

for file_name in os.listdir(my_path):
	print(os.path.join(my_path, file_name))

file_matches = os.path.join(my_path, "*.png")
print("All PNG files in the Images folder:")
for file_name in glob.glob(file_matches):
	print(file_name)

## Rename any PNG files in the images folder and its subfolders to be JPG files by using os.walk()
for current_folder, subfolders, files_names in os.walk(my_path):
	for file_name in files_names:
		file_path = os.path.join(current_folder, file_name)
		file_tuple = os.path.splitext(file_path) # split into (path, extension)
		if file_tuple[1].lower() == ".png": # check if extension is PNG
			os.rename(file_path, file_tuple[0] + ".jpg")


