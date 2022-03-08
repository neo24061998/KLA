import csv

file = open('log.csv', 'w')

writer = csv.writer(file)

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

writer.writerow(header)
writer.writerow(data)

file.close()
