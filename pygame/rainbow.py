import pygame
import random

window_x = 300
window_y = 200

def get_rand_colour():
    colour_r = random.randint(0,255)
    colour_g = random.randint(0,255)
    colour_b = random.randint(0,255)
    return (colour_r,colour_g,colour_b)

screen = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Rainbow!")
clock = pygame.time.Clock()

done = False
counter = 0
colour = get_rand_colour()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    counter += 1
    if counter > 3:
        colour = get_rand_colour()
        counter = 0

    screen.fill(colour)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()