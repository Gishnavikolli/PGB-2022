#6. Write a Python program that reads each row of a given csv file and skip the header of the file. Also print the number of rows and the field names.
import csv
fields = []
rows = []
with open('Day9/sample.csv', newline='') as csvf:
 info = csv.reader(csvf, delimiter=' ')
 fields = next(info)
 for row in info:
   pass
print("\nTotal no. of rows: %d"%(info.line_num))
print('Field names are:')
print(', '.join(field for field in fields))