''' Images references
https://www.behance.net/gallery/41046589/Planet-Orb-2/modules/548523771
https://www.pinterest.com/pin/4151824652646010/
https://dribbble.com/shots/4465418-Energy-Sphere
https://www.deviantart.com/nightrainexplorer/art/Our-Magic-750765641
https://www.pinterest.com/pin/1688918606938935/
https://www.pinterest.com/pin/433190057925201870/
'''
import os
import pygame
import tkinter as tk
from tkinter import *
import time
clock = pygame.time.Clock()

root = tk.Tk()
embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(255,255,255))
pygame.display.init()

value = 0

image_sprite = [pygame.image.load(),
      # Put all images you want to load here
               ]
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    if value > y:
        value = 0
    image = image_sprite[value]
    x = 50
    y = 100
    screen.blit(image, (0, 0))
    pygame.display.update()
    screen.fill((0, 0, 0))
    value += 1
    root.update()
