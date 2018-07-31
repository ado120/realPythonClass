my_output_file = open("hello.txt", "w")

lines_to_write = ["This is my file.", "\nThere are many like it,", "\nbut this one is mine."]

my_output_file.writelines(lines_to_write)
my_output_file.close()