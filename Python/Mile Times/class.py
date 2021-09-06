from miletimes import Miles
import pandas as pd
import re


class Miles_times():
    def __init__(self):
        self.file = 'mile_times.csv'
        
    def new_time(self):
        while 1:
            date = input("Enter date (MM/DD/YYYY): ")
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
                print("Invalid format")
                continue
        with open(self.file, 'a') as mt:
            mt.write("\n" + date[:5] + "," + ("-," * (year-2018)) + time)
            mt.close()
        df = pd.read_csv(self.file)
        df = df.sort_index(axis=0, ascending = True)
        df = df.fillna('-')
        df
        
        
if __name__=='__main__': 
    Miles_times().new_time()
