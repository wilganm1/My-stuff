""" Comma Separated Values """
column1 data, column2 data, column3 data
first row data 1, first row data 2, first row data 3
second row data 1, second row data 2, second row data 3
...

#Delimiters, what separates values
\t   -tab
:    -colon
;    -semi-colon

""" Reading csv with csv package """
import csv

with open("file.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_render:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

""" Writing CSV files """
#csv.writer object to create the 
import csv

with open('file.csv', mode='w') as file:
    file_writer= csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file_writer.writerow(['a','b','c']) #1st row
    file_writer.writerow(['e','f','g']) #2nd row

#Write from a dictionary
with open('file.csv', mode='w') as file:
    fieldnames = ['1','2','3']
    writer = csv.DictWriter(csv_file, fieldnames-fieldnames)

    writer.writeheader()    
    writer.writerow({'1': 'a','b','c'}) #1st row
    writer.writerow({'1': 'e','f','g'}) #2nd row
    
""" Using pandas """
#Pandas reads csv into a dataframe
import pandas
df = pandas.read_csv(
    'file.csv',
    index_col='Name', #changes index col name
    parse_dates=['Hire Date'] #YYYY-MM--DD
    header = 0,  #ignores existing col names
    names = ['a','b','c']) #names of columns

""" Writing csv with pandas """
#You aren't writing a new file, just modifying

df.to_csv('file.csv')
