import pygame
import random
import time
import os
import math

pygame.font.init()

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHOOTER")       #Name of the game

enemy_count = 1  #set default enemy number
#starting position of triangle
point1 = [WIDTH/8 - WIDTH/16, HEIGHT/2 - HEIGHT/16]
point2 = [WIDTH/8, HEIGHT/2]
point3 = [WIDTH/8 - WIDTH/16, HEIGHT/2 + HEIGHT/16]

triangle_vertices = [point1, point2, point3]

   # Random numbers that are subtracted from initial enemy cooridnates
random_x = random.uniform(0, WIDTH/4 - 1)
random_y = random.uniform(0, HEIGHT/9/16 - 1)
#enemy starting point
enemy_point1 = [WIDTH * 0.75 + WIDTH/16 - random_x, HEIGHT/2 - HEIGHT/16 - random_y]
enemy_point2 = [WIDTH * 0.75 - random_x, HEIGHT/2 - random_y]
enemy_point3 = [WIDTH * 0.75 + WIDTH/16 - random_x, HEIGHT/2 + HEIGHT/16 - random_y]
enemy_triangle = [enemy_point1, enemy_point2, enemy_point3]
       
velocity = 10
bg = pygame.image.load('C:/Users/WilganZMT/Pictures/black screen.png') 
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
    screen.blit(bg, (0,0))    # THIS RESETS THE BACKGROUND WHEN BULLETS ARE FIRED
    for bullet in enemy_bullets:
        bullet.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.draw.polygon(screen, "red", enemy_triangle)
    pygame.draw.polygon(screen, "green", triangle_vertices)

    pygame.display.update()

bullets = []  #SINCE BULLTS ARE OBJECTS THAT GET CREATED THEY ARE STORED HERE     
enemy_bullets = []
GAME_OVER = False

running = True
xr = [-1,1]
yr = [-1,1]

vel_x = random.choice(xr)
vel_y = random.choice(yr)

player_health = 3
enemy_health = 3

random_fire = [40,50,60,70,80,90] 
fire_choice = random.choice(random_fire)     


GAME_OVER = False   # WHEN SOMEONE WINS MAKE THIS TRUE AND HAVE A MESSAGE POP UP 
while not GAME_OVER:
    while running:
        clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # fill the screen with a color to wipe away anything from last frame        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and triangle_vertices[0][1] > 0 or keys[pygame.K_UP] and triangle_vertices[0][1] > 0:
            for point in triangle_vertices:
                point[1] -= velocity
        if keys[pygame.K_s] and triangle_vertices[2][1] < HEIGHT or keys[pygame.K_DOWN] and triangle_vertices[2][1] < HEIGHT:
            for point in triangle_vertices:
                point[1] += velocity
        if keys[pygame.K_a] and triangle_vertices[0][0] > 0 or keys[pygame.K_LEFT] and triangle_vertices[0][0] > 0  :
            for point in triangle_vertices:
                point[0] -= velocity
        if keys[pygame.K_d] and triangle_vertices[1][0] < WIDTH/2 or keys[pygame.K_RIGHT] and triangle_vertices[1][0] < WIDTH/2:
            for point in triangle_vertices:
                point[0] += velocity
                
        if keys[pygame.K_SPACE]:
            if len(bullets) == 0 :        # NUMBER OF BULLTS ALLOWED, DELETE FOR INFINITE
                bullets.append(Projectile(triangle_vertices[1][0], triangle_vertices[1][1], 10, 'yellow'))
            if len(bullets) > 0 and len(bullets) < 2:
                for bullet in bullets:
                    if bullet.x > triangle_vertices[1][0] + WIDTH/2:   
                        bullets.append(Projectile(triangle_vertices[1][0], triangle_vertices[1][1], 10, 'yellow'))
        
        for bullet in bullets:                   #THIS BLOCK CAUSES THE BULLETS TO FLY
            if bullet.x < WIDTH and bullet.x > 0:
                bullet.x += velocity * 3  #This causes the bullets to move
            else:
                bullets.pop(bullets.index(bullet))  #ONCE BULLET HITS EDGE IT DISAPPEARS        
                  
        if pygame.time.get_ticks() % 50 == 0:
            vel_x = random.choice(xr)
            vel_y = random.choice(yr)
                
        if enemy_triangle[1][0] >= WIDTH/2 and enemy_triangle[0][0] < WIDTH + velocity:
            for point in enemy_triangle:
                point[0] += velocity * vel_x     #RANDOM X
        elif enemy_triangle[1][0] < WIDTH/2 + velocity +1 :  #check left wall
             for point in enemy_triangle:
                 point[0] += velocity
        elif enemy_triangle[0][0] >= WIDTH:  #check right wall
             for point in enemy_triangle:
                 point[0] -= velocity
                 
        if enemy_triangle[0][1] >= 0 - velocity - 1 and enemy_triangle[2][1] < HEIGHT + velocity :
            for point in enemy_triangle:       # Random Y
                point[1] += velocity * vel_y
        elif enemy_triangle[0][1] <= 0: #check top wll
            for point in enemy_triangle:
                point[1] += velocity * 2
        elif enemy_triangle[2][1] >= HEIGHT: #check bottom wall
            for point in enemy_triangle:      
                point[1] -= velocity * 2
                
        random_fire = [40,50,60,70]
        fire_choice = random.choice(random_fire)
        if pygame.time.get_ticks() % fire_choice == 0:
            enemy_bullets.append(Projectile(enemy_triangle[1][0], enemy_triangle[1][1], 10, 'yellow'))                    
        for bullet in enemy_bullets:                   #THIS BLOCK CAUSES THE BULLETS TO FLY
            if bullet.x < WIDTH and bullet.x >= 0:
                bullet.x -= velocity * 4  #This causes the bullets to move
            else:
                enemy_bullets.pop(enemy_bullets.index(bullet))  #ONCE BULLET HITS EDGE IT DISAPPEARS        
        redrawGameWindow()  
    
        if len(bullets) > 0:
            for bullet in bullets:
                if bullet.x >= enemy_triangle[1][0] and bullet.x <= enemy_triangle[0][0] and bullet.y >= enemy_triangle[1][1] and bullet.y <= enemy_triangle[0][1]:
                    bullets.pop(bullets.index(bullet))
                    enemy_health -= 1
                else: 
                    pass
            
        """
        
        Bullet not disappearing when hitting triangle
        
        Make it so that any pixel inside the are of the cirlce counts
        
        bullet area = math.pi * 10 ** 2
        
        
        collison: 
            
        if any point of the circumference of the bullet touches 
        any point of the triangle then collision = True
        
        The point of contact has (x,y) coordinates
        
        So basically the radius has to touch the triangle.
        The radius has an x displacement and a y displacement.
        
        Just use pythagorian's theorem. Round down to nearest pixel
        
        
        
        """

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            
        pygame.draw.line(screen, "white", (WIDTH/2,0),(WIDTH/2,HEIGHT))
              
        pygame.display.flip()
    
    if player_health <= 0:
        GAME_OVER = True
    elif enemy_health <= 0:
        GAME_OVER = True
    
    
    pygame.quit()
       
