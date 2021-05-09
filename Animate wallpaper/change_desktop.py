import ctypes
import glob
import time
from PIL import Image
from datetime import datetime

water_list = []    #list name
for filename in glob.glob("pic folder 1 path/*.png"):  #change to your path
    im = Image.open(filename)
    water_list.append(im)

#You can use a function command, but I'm going to put this into an exe file, so I exclude it.
while True:
    while 7 <= datetime.now().hour < 15:   #Sets when it happens according to time of day on your system.
        for n in range(len(water_list)):
            time.sleep(0.05)
            ctypes.windll.user32.SystemParametersInfoW(20,0, "pic folder 1 path" + str(n) + "_delay-0.03s.png", 0)
            continue
"""           




Add more here




"""
