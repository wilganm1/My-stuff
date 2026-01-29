import pygame
import os

''' Images references
https://www.behance.net/gallery/41046589/Planet-Orb-2/modules/548523771
https://www.pinterest.com/pin/4151824652646010/
https://dribbble.com/shots/4465418-Energy-Sphere
https://www.deviantart.com/nightrainexplorer/art/Our-Magic-750765641
https://www.pinterest.com/pin/1688918606938935/
https://www.pinterest.com/pin/433190057925201870/
'''


# Initialize pygame (essential for image loading/handling)
pygame.init()

# Define image folder path and an empty list to store the images
image_folder = "your_image_folder" # Replace with your folder path
images = []

# Loop through files in the folder and load them if they end with .png
for filename in os.listdir(image_folder):
    if filename.endswith(".png"):
        path = os.path.join(image_folder, filename)
        # Load the image and convert it for faster blitting
        img = pygame.image.load(path).convert_alpha()
        images.append(img)
