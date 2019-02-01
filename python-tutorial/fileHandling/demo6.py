# file handling example
import csv

# open data.csv file
with open('data.csv') as csvfile:
    names=[]
	# read data from csv
    readcsv=csv.reader(csvfile,delimiter=',')
    for row in  readcsv:
        name=row[0]
        names.append(name)
# print the list of names
print(names)
