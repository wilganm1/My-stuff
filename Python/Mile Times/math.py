import pandas as pd
from miletimes import Miles
# Loop through dictionary and add up seconds and minutes
minutes, seconds = 0, 0

for year in Miles:
    for minute in Miles[year].values():
        minutes += int(minute[0])
    for second in Miles[year].values():
        seconds += int(second[2:])


min_to_sec = minutes * 60
total = min_to_sec + seconds
total
# 24442 total seconds

# Now to find the average
runs = 0
for dates in Miles:
    runs += len(Miles[dates])

runs
# 59

average = 24442 / 59
average
# 414.271186440678 seconds

414.271186440678 / 60

60 * .9045197740113

Averge_time = "6:54"
