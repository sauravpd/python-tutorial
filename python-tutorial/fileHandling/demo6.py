import csv

with open('data.csv') as csvfile:
    names=[]
    readcsv=csv.reader(csvfile,delimiter=',')
    for row in  readcsv:
        name=row[0]
        names.append(name)
print(names)
