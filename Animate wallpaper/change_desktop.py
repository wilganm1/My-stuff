import ctypes
import glob
import time
from PIL import Image
from datetime import datetime

water_list = []
for filename in glob.glob("pic folder 1 path/*.png"):  #change to your path
    im = Image.open(filename)
    water_list.append(im)

lake_list = []
for filename in glob.glob("pic folder 2 path/*.png"):
    zo = Image.open(filename)
    lake_list.append(zo)

universe_list = []
for filename in glob.glob("pic folder 3 path/*.png"):
    tq = Image.open(filename)
    universe_list.append(tq)

def animate():
    while True:
        while 7 <= datetime.now().hour < 15:
            for n in range(len(water_list)):
                time.sleep(0.05)
                ctypes.windll.user32.SystemParametersInfoW(20,0, "pic folder 1 path" + str(n) + "_delay-0.03s.png", 0)
                continue
        while 15 <= datetime.now().hour < 20:
            for nm in range(len(universe_list)):
                time.sleep(0.05)
                ctypes.windll.user32.SystemParametersInfoW(20,0, "pic folder 2 path" + str(nm) + "_delay-0.1s.png", 0)
                continue
        while 20 <= datetime.now().hour <= 24 or 0 <= datetime.now().hour < 7 :
            for nm in range(len(lake_list)):
                time.sleep(0.05)
                ctypes.windll.user32.SystemParametersInfoW(20,0, "pic folder 3 path" + str(nm) + "_delay-0.06s.png", 0)
                continue
            continue
