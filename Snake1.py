import pygame
import random
import os

pygame.mixer.init()

pygame.init()

#use color using (r, g, b) values red, green, blue
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width, screen_height))

bgimg = pygame.image.load("Snake3.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("Snake Game")
pygame.display.update()
Clock = pygame.time.Clock()
Font = pygame.font.SysFont(None, 55)

# with open("HighScore.txt", "r") as f:
#     highscore = f.read()

def text_screen(text, color, x, y):
    screen_text = Font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gamewindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow, color,[x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((101,189,229))
        text_screen("Welcome to Snake Game", black, 260, 250)
        text_screen("Press Enter to play", black, 262, 300)
        text_screen("- Created By BHUVAN", black, 270, 360)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # pygame.mixer.music.load('Game1music.mp3')
                    # pygame.mixer.music.play()
                    game_loop()
        
        pygame.display.update()
        Clock.tick(30)

def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    score = 0
    snake_size = 10
    fps = 30
    food_x = random.randint(20, screen_width/1.5)
    food_y = random.randint(20, screen_height/1.5)

    snake_list = []
    snake_length = 1
    #for checking highscore file is exist or not
    if(not os.path.exists("HighScore.txt")):
        with open("HighScore.txt", "w") as f:
            f.write("0")

    with open("HighScore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("HighScore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.fill((200,200,50))
            text_screen("Game Over! Press enter to continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # snake_x = snake_x + 10
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        # snake_x = snake_x - 10
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        # snake_y = snake_y - 10
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        # snake_y = snake_y + 10
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 1
                pygame.mixer.music.load('Ding.mp3')
                pygame.mixer.music.play()
                print("Score: ", score)
                food_x = random.randint(20, screen_width/1.5)
                food_y = random.randint(20, screen_height/1.5)
                snake_length += 5
                if score> int(highscore):
                    highscore = score
        
            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0,0))
            text_screen("Score: " +str(score)+ "  Highsore: " +str(highscore), red, 5, 5)
            pygame.draw.rect(gamewindow,red,[food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('Gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('Gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gamewindow, black, snake_list, snake_size)

        pygame.display.update()
        Clock.tick(fps)


    pygame.quit()
    quit()

welcome()