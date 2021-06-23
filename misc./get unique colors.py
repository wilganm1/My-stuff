import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread(' ~~ Insert file here ~~ ')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  #Need to convert to RGB for correct colors
image = np.array(image, dtype = int)
plt.imshow(image)

image = np.unique(image.reshape(-1, img.shape[-1]), axis=0, return_counts=True)
unique_list = []
for x in image:
    unique_list.append(x)
unique_list = unique_list[0]
unique_list         #matrix of every single color in rgb format.
len(unique_list)   #How many unique colors are in image.
