import csv

MY_FILE = "./data/sample_sfpd_incident_all.csv"
def parse(raw_file, delimiter):

	opened_file = open(raw_file) #open & close CSV file

	csv_data = csv.reader(opened_file, delimiter=delimiter) #read CSV data

	parsed_data = [] #setup empty list 

	#skip over the first line (used for headers)
	fields = next(csv_data)

	#for each row in csv file, zip together field->value 
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	#close CSV file
	opened_file.close()

	return parsed_data






def main():
	new_data = parse(MY_FILE, ",")

	print(new_data)


if __name__ == "__main__":
	main()