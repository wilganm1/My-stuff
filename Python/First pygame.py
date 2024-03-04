"""
I want to a make a alien shooter game like asteroid except it's just
me vs CPU. I will have the entire left side of the screen and the 
enemies will have the right side of the screen. All enemies will be in
the same surface to make everthying easier. They won't be affected by
their own attacks and won't have collsion'

Each enemy needs its own rectangle for its traingle to be in.
"""
import pygame
import random
import time
import os
pygame.font.init()

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHOOTER")       #Name of the game

enemy_count = 1  #set default enemy number
#starting position of triangle
point1 = [WIDTH/4 - WIDTH/16, HEIGHT/2 - HEIGHT/16]
point2 = [WIDTH/4, HEIGHT/2]
point3 = [WIDTH/4 - WIDTH/16, HEIGHT/2 + HEIGHT/16]

triangle_vertices = [point1, point2, point3]


"""
Need variables for all 4 directions then randomly choose one.

We need all 4 because you up down left and right spawn points have to be 
within the box. 

So make 4 variables then randomly choose between them.

"""

   # Random numbers that are subtracted from initial enemy cooridnates
random_x = random.uniform(0, WIDTH/4 - 1)
random_y = random.uniform(0, HEIGHT/9/16 - 1)


#enemy starting point
enemy_point1 = [WIDTH * 0.75 + WIDTH/16 - random_x, HEIGHT/2 - HEIGHT/16 - random_y]
enemy_point2 = [WIDTH * 0.75 - random_x, HEIGHT/2 - random_y]
enemy_point3 = [WIDTH * 0.75 + WIDTH/16 - random_x, HEIGHT/2 + HEIGHT/16 - random_y]
enemy_triangle = [enemy_point1, enemy_point2, enemy_point3]

"""old enemy starting point. bottom right corner
enemy_point1 = [WIDTH * 0.75 + WIDTH/16 - random_x, HEIGHT/2 - HEIGHT/16 - random_y]
enemy_point2 = [WIDTH * 0.75 - random_x, HEIGHT/2 - random_y]
enemy_point3 = [WIDTH * 0.75 + WIDTH/16 - random_x, HEIGHT/2 + HEIGHT/16 - random_y]
enemy_triangle = [enemy_point1, enemy_point2, enemy_point3]
"""



enemy_triangle = [enemy_point1, enemy_point2, enemy_point3]


"""
The enemy triangle now maintains a constant direction but it 
now wants to go to the top left corner by default.

        This is becasue of the way its spawned. Its spawn is bottom right
        and random values are subtracted from there so every subtraction 
        is just getting closer to the top left corner


Another problem is that when it hits one of the 4 edges it stops 
moving in the respective direction.

    -For example: When it hits the back side wall it still goes up and down
                  but won't move away from the wall.

Write code so that it will automatically eject 
"""
       

velocity = 5

def shoot(x_pos, y_pos):
    pygame.draw.circle(screen, "yellow", [x_pos, y_pos], 10)

running = True
r = [-1,1]
while running:
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player = pygame.draw.polygon(screen, "green", triangle_vertices)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and triangle_vertices[0][1] > 0 or keys[pygame.K_UP] and triangle_vertices[0][1] > 0:
        for point in triangle_vertices:
            point[1] -=5
    if keys[pygame.K_s] and triangle_vertices[2][1] < HEIGHT or keys[pygame.K_DOWN] and triangle_vertices[2][1] < HEIGHT:
        for point in triangle_vertices:
            point[1] +=5
    if keys[pygame.K_a] and triangle_vertices[0][0] > 0 or keys[pygame.K_LEFT] and triangle_vertices[0][0] > 0  :
        for point in triangle_vertices:
            point[0] -= 5
    if keys[pygame.K_d] and triangle_vertices[1][0] < WIDTH/2 or keys[pygame.K_RIGHT] and triangle_vertices[1][0] < WIDTH/2:
        for point in triangle_vertices:
            point[0] += 5
    if keys[pygame.K_SPACE]:
        shoot(triangle_vertices[1][0], triangle_vertices[1][1])
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        
    enemy = pygame.draw.polygon(screen, "red", enemy_triangle)
      
    if pygame.time.get_ticks() % 10 == 0:
        vel_r = random.choice(r)
    if enemy_triangle[0][1] > 0 and enemy_triangle[2][1] < HEIGHT:    #RANDOM Y
        for point in enemy_triangle:    # Random 
            point[1] += velocity * vel_r
    if enemy_triangle[1][0] > WIDTH/2 + velocity + 1 and enemy_triangle[0][0] < WIDTH:
        for point in enemy_triangle:
            point[0] += velocity * vel_r     #RANDOM X
                            
    pygame.draw.line(screen, "white", (WIDTH/2,0),(WIDTH/2,HEIGHT))
          
    pygame.display.flip()

pygame.quit()
