import pandas as pd
import matplotlib.pyplot as plt
import re
import random as rnd

class Time_math():
    def __init__(self):
        self.df = pd.read_csv('mile_times.csv')
        self.df = self.df.sort_index(axis=0, ascending = True)
        self.df = self.df.fillna('-')
        self.minutes = 0
        self.seconds = 0
        self.min_to_sec = None
        self.total = None
        self.runs = len(self.df)
        self.average_sec = None
        self.avg_sec_to_min = None
        self.remainder = None
        self.true_sec = None
        self.average_time = None
        self.Averages = {}
        self.x_axis = None
        self.y_axis = None
        self.bar_colors = None
        self.bar_times = None
                
    def new_time(self):
        entry = input("Enter new time? (y/n): ")
        if entry == 'y':
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
            with open('mile_times.csv', 'a') as mt:
                mt.write("\n" + date[:5] + "," + ("-," * (year-2018)) + time)
                mt.close()
            self.math()
        else:
            self.math()
            
    def math(self):
        print(self.df)
        for year in self.df.columns:
            for time in self.df[year]:
                if time != "-":
                    self.minutes += int(time[0])
                    self.seconds += int(time[2:])
        self.min_to_sec = self.minutes * 60
        self.total_sec = self.min_to_sec + self.seconds
        self.average_sec = self.total_sec/self.runs
        self.avg_sec_to_min = self.average_sec/60
        self.remainder = self.avg_sec_to_min % 1
        self.true_sec = int(round(self.remainder *60,0))
        self.average_time = str(int(round(self.avg_sec_to_min, 0))) + ':' + str(self.true_sec)
        print("Average Time is: " + self.average_time)
        self.plot()
        
    def plot(self):
        for column in self.df.columns:
            self.Averages[column] = [times for times in self.df[column] if times != '-']           
        for avg in self.Averages:
            self.Averages[avg] = round((sum([int(g[0])*60 for g in self.Averages[avg]] + [int(g[2:]) for g in self.Averages[avg]])/60)/len(self.Averages[avg]),1)
        self.x_axis = [a for a in self.Averages]
        self.y_axis = [self.Averages[t] for t in self.Averages]
        self.bar_colors = [tuple([round(rnd.random(),1) for x in range(0,3)]) for x in range(len(self.Averages))]
        plt.bar(self.x_axis, self.y_axis,
                align = 'center',
                color = self.bar_colors)
        plt.title("Average Mile Times")
        plt.xlabel("Years")
        plt.ylabel("Average Time")
        plt.text = [self.Averages[y] for y in self.Averages]
        plt.show()
#make a list for every year       
if __name__=='__main__': 
    Time_math().new_time()
