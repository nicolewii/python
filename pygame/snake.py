import pygame
import random
#used the tutorial of https://www.edureka.co/blog/snake-game-with-pygame/, but adding a few extra twists.

#red - food (+1)
#purple - poision (-1)
#white - speed boost
#brown - slow down (like mud)
#gray - obstacle (end game)
#outside of bounds (end game)
#rainbow - creates a lot of food (+however many to eat for certain amount of time)

#includes: a high score feature and lists stats at the end of the game. 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
purple = (162, 0, 255)
gray = (186, 186, 186)
brown = (130, 59, 0)
 
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 18


font_style = pygame.font.SysFont("arial", 30)
score_font = pygame.font.SysFont("arial", 20)
info_font = pygame.font.SysFont("arial", 25)
title_font = pygame.font.SysFont("impact", 40)
warn_font = pygame.font.SysFont("arial", 30)
score_list = [0]

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def High_score(score, score_list):
    if score > score_list[0]:
        score_list.append(score)
        score_list.sort(reverse=True)
    value = score_font.render("High Score: " + str(score_list[0]), True, white)
    dis.blit(value, [0, 22])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width /4, dis_height /3])

def info():
    info = True
    while info:
        dis.fill(black)
        text = info_font.render("Green - Snake", True, green) 
        dis.blit(text, [200, 25])
        text = info_font.render("Red - Apple (+1)", True, red) 
        dis.blit(text, [200, 50])
        text = info_font.render("Purple - Poison (-1)", True, purple) 
        dis.blit(text, [200, 75])
        text = info_font.render("Gray - Wall (Obstacle to Avoid)", True, gray) 
        dis.blit(text, [200, 100])
        text = info_font.render("Brown - Mud (Slows snake down)", True, brown) 
        dis.blit(text, [200, 125])
        text = info_font.render("White - Speed Pill (Speeds snake up)", True, white) 
        dis.blit(text, [200, 150])
        text = info_font.render("Rainbow - Speed Pill (Speeds snake up)", True, get_rand_colour()) 
        dis.blit(text, [200, 175])
        text = info_font.render("Note: You cannot press left then right or up then down", True, white)
        dis.blit(text, [200, 200])
        text = info_font.render("   and vice versa when the snake is bigger than 2", True, white) 
        dis.blit(text, [200, 225])
        text = info_font.render("   due to the game considering that a snake colliding with itself", True, white) 
        dis.blit(text, [200, 250])
        if start_button_info.draw(dis):
            gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                info = False
        pygame.display.update()
def range_with_floats(start, stop, step):
    while stop > start:
        yield start
        start += step
def get_rand_colour():
    colour_r = random.randint(0,255)
    colour_g = random.randint(0,255)
    colour_b = random.randint(0,255)
    return (colour_r,colour_g,colour_b)
def gameLoop():
    game_over = False
    game_close = False

    snakesp = snake_speed
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
    
    wallw = 10
    wallh = random.randint(20, 300)*1.0
    
    mudw = random.randint(70, 170)*1.0
    mudh = random.randint(70, 170)*1.0
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    poisionx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    poisiony = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    wallx = round(random.randrange(0, dis_width - int(wallw)) / 10.0) * 10.0
    wally = round(random.randrange(0, dis_height - int(wallw)) / 10.0) * 10.0

    speedx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    speedy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    mudx = round(random.randrange(0, dis_width - int(mudw)) / 10.0) * 10.0
    mudy = round(random.randrange(0, dis_height - int(mudh)) / 10.0) * 10.0
    inmud = False
    
    rainx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    rainy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press P-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            score_list.append(Length_of_snake -1)
            High_score(Length_of_snake -1, score_list)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        colour = get_rand_colour()
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, purple, [poisionx, poisiony, snake_block, snake_block])
        if len(snake_List) > 2:
            pygame.draw.rect(dis, gray, [wallx, wally, wallw, wallh])
        if len(snake_List) > 3:
            pygame.draw.rect(dis, brown, [mudx, mudy, mudw, mudh])
        if len(snake_List) > 4:
            pygame.draw.rect(dis, white, [speedx, speedy, snake_block, snake_block])
        if (len(snake_List)-1) % 10 == 0 and len(snake_List) != 1:
             pygame.draw.rect(dis, colour, [rainx, rainy, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        High_score(Length_of_snake -1, score_list)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            poisionx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            poisiony = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            wallx = round(random.randrange(0, dis_width - int(wallw)) / 10.0) * 10.0
            wally = round(random.randrange(0, dis_height - int(wallw)) / 10.0) * 10.0
            mudx = round(random.randrange(0, dis_width - int(mudw)) / 10.0) * 10.0
            mudy = round(random.randrange(0, dis_height - int(mudh)) / 10.0) * 10.0
            speedx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            speedy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            rainx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            rainy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            wallh = random.randint(20, 300)*1.0
    
            mudw = random.randint(70, 170)*1.0
            mudh = random.randint(70, 170)*1.0

            Length_of_snake += 1
        if x1 == poisionx and y1 == poisiony:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            poisionx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            poisiony = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            wallx = round(random.randrange(0, dis_width - int(wallw)) / 10.0) * 10.0
            wally = round(random.randrange(0, dis_height - int(wallw)) / 10.0) * 10.0
            mudx = round(random.randrange(0, dis_width - int(mudw)) / 10.0) * 10.0
            mudy = round(random.randrange(0, dis_height - int(mudh)) / 10.0) * 10.0
            speedx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            speedy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            rainx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            rainy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            wallh = random.randint(20, 300)*1.0

            mudw = random.randint(70, 170)*1.0
            mudh = random.randint(70, 170)*1.0

            snake_List.pop()
            if len(snake_List) == 0:
                game_close = True 
                Your_score(0)
            else:
                Length_of_snake -= 1
                Your_score(Length_of_snake)
        if x1 in range_with_floats(mudx, mudx+mudw, 1.0) and y1 in range_with_floats(mudy, mudy+mudh, 1.0) and len(snake_List) > 3: 
            if not inmud:
                inmud = True
                if snakesp > 12:
                    snakesp -= 2
        if x1 not in range_with_floats(mudx, mudx+mudw, 1.0) and y1 not in range_with_floats(mudy, mudy+mudh, 1.0):
            inmud = False
        if x1 == speedx and y1 == speedy and len(snake_List) > 4:
            snakesp +=2
            speedx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            speedy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        if x1 == wallx and y1 in range_with_floats(wally, wally+wallh, 1.0) and len(snake_List) > 2:
            del snake_List[0]
            game_close = True
        if x1 == rainx and y1 == rainy and Length_of_snake % 2 == 0:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            poisionx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            poisiony = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            wallx = round(random.randrange(0, dis_width - int(wallw)) / 10.0) * 10.0
            wally = round(random.randrange(0, dis_height - int(wallw)) / 10.0) * 10.0
            mudx = round(random.randrange(0, dis_width - int(mudw)) / 10.0) * 10.0
            mudy = round(random.randrange(0, dis_height - int(mudh)) / 10.0) * 10.0
            speedx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            speedy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            rainx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            rainy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 5
            Your_score(Length_of_snake)
        clock.tick(snakesp)
 
    pygame.quit()
    quit()

#game start
start_img = pygame.image.load('snake-start.png').convert_alpha()
help_img = pygame.image.load('snake-help.png').convert_alpha()
quit_img = pygame.image.load('snake-quit.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self, dis):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        dis.blit(self.image, (self.rect.x, self.rect.y))

        return action
#start screen button
start_button = Button(300, 100, start_img, 1)
help_button = Button(300, 225, help_img, 1)
exit_button = Button(300, 350, quit_img, 1)
start_button_info = Button(300, 500, start_img, 1)
#start loop 
run = True
while run:
    dis.fill(black)
    text = title_font.render("Snake...but harder", True, green) 
    dis.blit(text, [275, 15])
    text = warn_font.render("WARNING: Contains flashing lights", True, red) 
    dis.blit(text, [235, 60])
    if start_button.draw(dis):
        gameLoop()
    if help_button.draw(dis):
        info()
    if exit_button.draw(dis):
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()