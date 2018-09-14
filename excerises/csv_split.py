import argparse
import csv
import os
import sys

"""
Splits a CSV file into multiple pieces based on command line arguments.
    Arguments:
    `-h`: help file of usage of the script
    `-i`: input file name
    `-o`: output file name
    `-r`: row limit to split
    Default settings:
    `output_path` is the current directory
    headers are displayed on each split file
    the default delimeter is a comma
    Example usage:
    ```
    # split csv by every 100 rows
    >> python csv_split.py -i input.csv -o output -r 100
    ```
"""

def arguments():
	parser = argparse.ArgumentParser(description='Test..')
	parser.add_argument("-i", "--input-file", required=True, help="input file name")
	parser.add_argument("-o", "--output-file", required=True, help="output file name")
	parser.add_argument("-r", "--row-limit", required=True, help="row limit to split", type=int)
	args = parser.parse_args()

	is_valid_file(parser, args.input_file)

	is_valid_csv(parser, args.input_file, args.row_limit)

	return args.input_file, args.output_file, args.row_limit

def is_valid_file(parser, file_name):
	"""Ensure that the input_file exists"""
	if not os.path.exists(file_name):
		parser.error("The file {} does not exist".format(file_name))
		sys.exit(1)

def is_valid_csv(parser, file_name, row_limit):
	"""
	Ensure that the # of rows in the input_file
	is greater than the row_limit.
	"""
	row_count = 0
	for row in csv.reader(open(file_name)):
		row_count += 1
	if row_limit > row_count:
		parser.error("More rows than actual rows in the file")
		sys.exit(1) 

def parse_file(arguments):
	input_file = arguments[0]
	output_file = arguments[1]
	row_limit = arguments[2]
	output_path = '.' #current directory

	#read CSV, split into list of lists
	with open(input_file, 'r') as input_csv:
		datareader = csv.reader(input_csv)
		all_rows=[]
		for row in datareader:
			all_rows.append(row)

	header = all_rows.pop(0)

	#split lists into chunks
	current_chunk = 1
	for i in range(0, len(all_rows), row_limit):
		chunk=all_rows[i:i + row_limit] #single chunk

		current_output = os.path.join(
			output_path,
			"{}-{}.csv".format(output_file, current_chunk)
			)

		#add in header row
		chunk.insert(0, header)

		with open(current_output, "w") as output_csv:
			writer = csv.writer(output_csv).writerows(chunk)

		print()
		print("File saved as {}".format(current_output))
		print("Number of rows in this chunk {}".format(len(chunk)))
		print("Chunk #{}".format(current_chunk))

		#increment current chunk
		current_chunk += 1

if __name__ == "__main__":
	arguments = arguments()
	parse_file(arguments)

























