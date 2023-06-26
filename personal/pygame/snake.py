import pygame
#using https://pygame.readthedocs.io/ for documentaion
pygame.init()
 
BLACK = (0,0,0)
GREEN = (0, 225, 0)
 
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Edureka')
 
game_over = False
 
x = 300
y = 300
 
x_change = 0       
y_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 10
                x_change = 0
            elif event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
 
    x += x_change
    y += y_change
    dis.fill(BLACK)
    pygame.draw.rect(dis, GREEN, [x, y, 10, 10])
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()