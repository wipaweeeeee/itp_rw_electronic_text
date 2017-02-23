import csv

with open('me_to_mom.csv', 'rb') as f:
	mycsv = csv.reader(f)
	mycsv = list(mycsv)
	line_number = len(mycsv)

	for i in range(line_number):
		text = mycsv[i][3]
		print text