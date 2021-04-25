import ctypes
import glob
import time
from PIL import Image

#Make a list and add all images
image_list = []
for filename in glob.glob("C:/Users/WilganZMT/Documents/Coding/Python/Animation Background/pics/Water ripple/*.png"):
    im = Image.open(filename)
    image_list.append(im)

len(image_list)   #60 images

pics={}        #empty dictionary to fill later
    
for img in image_list:
    for i in range(len(image_list)):
        pics[f"{i}"] = "C:/Users/WilganZMT/Documents/Coding/Python/Animation Background/pics/Water ripple/frame_" + str(img) + "_delay-0.03s.png"  

def animate():
    while True:
        for n in range(len(image_list)):
            time.sleep(0.05)
            ctypes.windll.user32.SystemParametersInfoW(20,0, "C:/Users/WilganZMT/Documents/Coding/Python/Animation Background/pics/Water ripple/frame_" + str(n) + "_delay-0.03s.png", 0)
        continue
