import ctypes
import glob
import time
from PIL import Image

#Make a list and add all images
#Change the directory and image to your own
image_list = []
for filename in glob.glob("C:/Users/WilganZMT/Documents/Coding/Python/Animation Background/pics/Water ripple/*.png"):
    im = Image.open(filename)
    image_list.append(im)

len(image_list)   #60 images

def animate():
    while True:            #The while loop keeps the animation running constantly.
        for n in range(len(image_list)):
            time.sleep(0.05)
            ctypes.windll.user32.SystemParametersInfoW(20,0, "C:/Users/WilganZMT/Documents/Coding/Python/Animation Background/pics/Water ripple/frame_" + str(n) + "_delay-0.03s.png", 0)
        continue
