import csv

# with open('data.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

#
# with open('data.csv','r') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter=',')
#
# 	for Column in csv_reader:
# 		print(Column[2])


# initializing the titles and rows list
fields = []
rows = []
filename="data.csv"
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row[4])

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')
