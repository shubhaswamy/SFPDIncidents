#take parsed data and visualize it ising Python math libraries


from collections import Counter

import csv
import matplotlib.pyplot as plt 
import numpy as np

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


def visualize_days():
	#visualize data by the day of the week

	data_file = parse(MY_FILE, ",")

	#counter = dictionary where it sums the total values for each key
	#keys = daysOfWeek; value = count of incidents 
	counter = Counter(item["DayOfWeek"] for item in data_file)

	data_list = [counter["Monday"], counter["Tuesday"], counter["Wednesday"], counter["Thursday"], counter["Friday"], counter["Saturday"], counter["Sunday"]]

	day_tuple = tuple(["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"])

	#assigning the data to a plot
	plt.plot(data_list)
	plt.xticks(range(len(day_tuple)), day_tuple)

	#save graph as 
	plt.savefig("Days.png")

	#close figure
	plt.clf()

def visualize_type():
	#visualize data by category in a bar graph 

	data_file = parse(MY_FILE, ",")
	counter = Counter(item["Category"] for item in data_file)

	#labels based on keys 
	labels = tuple(counter.keys())

	lenLabels = len(labels)

	#where the label is located on the x axis 
	#xlocations = np.arrange(lenLabels) + 0.5

	#width of each bar
	width = 0.5 

	#assign data to a bar plot
	plt.bar(xlocations, counter.values(), width = width)

	#assign labels and ticks to x-axis
	plt.xticks(xlocations + width /2, labels, rotation = 90)

	#adjust to give more room to labels
	plt.subplots_adjust(bottom = 0.4)

	#increase figure size 
	plt.rcParams['figure.figsize'] = 12, 8

	#Save the graph
	plt.savefig("Type.png")

	#close
	plt.clf()


def main():
	#visualize_days()
	visualize_type()

if __name__ == "__main__":
	main()