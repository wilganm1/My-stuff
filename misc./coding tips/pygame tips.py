"""This will teach you how to create pygames
with Python."""

"""All images/sounds/ etc will need to come
from a folder that's in the current 
directory the game file is in"""

#First import pygame
import pygame

#now  initialize pygame
pygame.init()

# Import pygame.locals for easier access to key coordinates
#These are the controls for the game
# Standard is that up = K_w
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT,
    K_RIGHT, K_ESCAPE, KEYDOWN, QUIT,)

#Make screen dimensions. Any size you want
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#   Add colors manually to be referenced later
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
orange = (255, 165, 0)
gray = (128,128,128)
purple = (128,0,128)
# https://www.rapidtables.com/web/color/RGB_Color.html#color-table


#  Adding in characters/environments with images
#  You can find custom pics online 
#   Use pygame.image.load
player = pygame.image.load(".png") #character


#      Sounds 
pygame.mixer.init()



#    Now keep running until told to stop
#    Each loop cycle is one frame
running = True
while running:
    
#Now make events. Events are things 
#the computer does when the user presses
#buttons. Each event has a type.
#KEYDOWN events are when you press down
#a key, like when to move.
    #look at every event in queue
    for event in pygame.event.get():
        #Did you hit a key?
        if event.type == KEYDOWN:
            #What is escape? If it was, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        
        #Did you click close window?
        #if yes, close the window
        elif event.type == QUIT:
            running = False
    #Get the set of keys pressed and check 
    #for user input
            
#Now add colors, sprites, surfaces,
#and combine them

    #Fill the background with color (r,g,b)
    #ranges from 0 - 225 for each
    screen.fill((white))
    #Now make a surface with its length and width
    surface = pygame.Surface(50, 50)
    #Give the surface color to separate it
    surface.fill((0,0,0))   #black
    

#Now we have to draw one image onto a surface
#Use blit to put one surface/image onto another
#blit mean block transfer
#Use blit on the surface drawn over
#blit is auto set on top-left corner of surface
#  need to center it 
    surface_center = (
        (screen_width-surface.get_width())/2,
        (screen_height-surface.get_height())/2)
 #source.blit(surface to draw, (location on source))
    screen.blit(surface, ((surface_center)))
    pygame.display.flip() #updates display
    #Add in the player with .blit()
    screen.blit(player, (1,1)) #player location
     
#Now add a clock to create a framerate
    clock = pygame.time.Clock()    
    # Flip everything to the display
    pygame.display.flip()
   # Ensure program maintains a rate of 
   # X frames per second
    clock.tick(30)  
    

#Now quit
pygame.quit()
quit()
