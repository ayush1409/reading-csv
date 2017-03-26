# reading the sample.csv file

import csv

with open("sample.csv") as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')
	print(readCSV)
	dates = []
	colors = []

	for row in readCSV:
		color = row[1]
		date = row[0]
		dates.append(date)
		colors.append(color)

try:
	x = input("which color's date you want to see : ")
	colorIndex = colors.index(x.lower())
	thedate = dates[colorIndex]
	print("\n the date is ",thedate," for color ",x)
except Exception as e:
	print(e)