import pygame
from pygame.locals import * 
from sys import exit
from random import randint


pygame.init()

collision_sound = pygame.mixer.Sound('smw_coin.wav')

WIDTH = 640
HEIGHT = 480

x_player = int(WIDTH/2)
y_player = int(HEIGHT/2)

speed = 10
x_control = speed
y_control = 0

x_obj_bruiser = randint(40, 600)
y_obj_bruiser = randint(50, 430)

points = 0

font = pygame.font.SysFont('arial', 40, True, True)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo_Teste")
clock = pygame.time.Clock()
snake_list = []

initial_lenght = 5

snake_dead = False

def snake_increases(snake_list):
    for XeY in snake_list:
        pygame.draw.rect(screen, (127.5,0,127.5), (XeY[0], XeY[1], 20, 20))


def game_reset():
    global points, initial_lenght, x_player, y_player, snake_list, head_list, x_obj_bruiser, y_obj_bruiser, snake_dead
    points = 0
    initial_lenght = 5
    x_player = int(WIDTH/2)
    y_player = int(HEIGHT/2)
    snake_list = []
    head_list = []
    x_obj_bruiser = randint(40, 600)
    y_obj_bruiser = randint(50, 430)
    snake_dead = False



while True:
    clock.tick(30)
    screen.fill((0,0,0))
    message = f'Points: {points}'
    formatted_text = font.render(message, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0
            if event.key == K_d:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0
            if event.key == K_w:
                if y_control == speed:
                    pass
                else:
                    x_control = 0
                    y_control = -speed
            if event.key == K_s:
                if y_control == -speed:
                    pass
                else:
                    x_control = 0
                    y_control = speed


    x_player = x_player + x_control
    y_player = y_player + y_control
            
    # if pygame.key.get_pressed()[K_a]:
    #     x_player = x_player - 20   
    # if pygame.key.get_pressed()[K_d]:
    #     x_player = x_player + 20
    # if pygame.key.get_pressed()[K_w]:
    #     y_player = y_player - 20
    # if pygame.key.get_pressed()[K_s]:
    #     y_player = y_player + 20     

    player = pygame.draw.rect(screen, (127.5,0,127.5), (x_player,y_player,20,20))
    object_bruiser = pygame.draw.rect(screen, (255,23.5,0), (x_obj_bruiser,y_obj_bruiser,20,20))

    if object_bruiser.colliderect(player):
        x_obj_bruiser = randint(40, 600)
        y_obj_bruiser = randint(50, 430)
        points = points + 1
        collision_sound.play()
        initial_lenght = initial_lenght + 1

    head_list = []
    head_list.append(x_player)
    head_list.append(y_player)

    
    snake_list.append(head_list)

    if snake_list.count(head_list) > 1:
        font2 = pygame.font.SysFont('arial', 20, True, True)
        message = 'Game Over! Press R key to play again'
        formatted_text = font2.render(message, True, (0,0,0))
        align_text = formatted_text.get_rect()

        snake_dead = True
        while snake_dead:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        game_reset()
            
            align_text.center = (WIDTH//2, HEIGHT//2)
            screen.blit(formatted_text, align_text)
            pygame.display.update()

    
    if x_player > WIDTH:
        x_player = 0
    if x_player < 0:
        x_player = WIDTH
    if y_player > HEIGHT:
        y_player = 0
    if y_player < 0:
        y_player = HEIGHT

                    

    if len(snake_list) > initial_lenght:
        del snake_list[0]

    snake_increases(snake_list)
    

    screen.blit(formatted_text, (430,40))

                    
    pygame.display.update()
    