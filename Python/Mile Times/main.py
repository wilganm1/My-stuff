from miletimes import Miles
import pandas as pd
import re

""" Make a function to append value to mile_times.csv
The format of the commas must be this:
        {year} 1,2,3,4
    date, -, -, - , time
    the number of commas indicates how the dataframe 
    will look. Make it so it auto-creates the 
    correct amount of {-,} before you input time"""

def new_time():
    while 1:
        date = input("Enter date (MM/DD/YYYY): ")
        if re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', date):
            pass
        else: 
            print("Invalid format. Try again.")
            continue
        year = int(date[-4:])
        if year < 2018:
            print("Year must be after 2018.")
            continue
        else:
            break
    while 1:
        time = input("Enter time (m:ss): ")
        if re.match('[0-9]{1}:[0-9]{2}', time):
            break
        else:
            print("Invalid format. Try again.")
            continue
    with open('mile_times.csv', 'a') as mt:
        mt.write("\n" + date[:5] + "," + ("-," * (year-2018)) + time)
        mt.close()
    df = pd.read_csv("mile_times.csv")
    df = df.sort_index(axis=0, ascending = True)
    df = df.fillna('-')
    df


""" Make the dataframe from the csv file """

if __name__=='__main__': 
    new_time()
