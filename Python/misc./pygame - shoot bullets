import pygame

pygame.init()
clock = pygame.time.Clock()

WIDTH = 500   
HEIGHT = 480

win = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('C:/Users/WilganZMT/Pictures/Wallpaper pics/sun set.jpg') 
        #######    NEED THIS    #######
        
class Projectile(object):   
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8     # THIS IS THE SPEED OF THE BULLET. 

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def redrawGameWindow():
    win.blit(bg, (0,0))    # THIS RESETS THE BACKGROUND WHEN BULLETS ARE FIRED
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()

#mainloop
bullets = []  #SINCE BULLTS ARE OBJECTS THAT GET CREATED THEY ARE STORED HERE                 
run = True
while run:
    clock.tick(27)   #FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:        # NUMBER OF BULLTS ALLOWED, DELETE FOR INFINITE
            bullets.append(Projectile('bullet x spawn', 'bullet y spawn', 10, 'green'))

    for bullet in bullets:                   #THIS BLOCK CAUSES THE BULLETS TO FLY
        if bullet.x < WIDTH and bullet.x > 0:    #
            bullet.x += bullet.vel   #This causes the bullets to move
        else:
            bullets.pop(bullets.index(bullet))  #ONCE BULLET HITS EDGE IT DISAPPEARS


    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        
    redrawGameWindow()

pygame.quit()
