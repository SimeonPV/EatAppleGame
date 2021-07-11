import pygame
from apple import Apple
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)

font = pygame.font.SysFont('roboto', 35)


WIDTH = 1000
HEIGHT = 600
serface = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('images/back1.jpg').convert()
score = pygame.image.load('images/score_fon.png').convert_alpha()
animal = pygame.image.load('images/animal.png').convert_alpha()
t_rect = animal.get_rect(centerx = WIDTH//2, bottom=HEIGHT-52)


counter = pygame.time.Clock()
FPS = 60

game_score = 0

apples = ({'path': 'redapple.png', 'score': 50},
              {'path': 'redapple2.png', 'score': 100},
              {'path': 'redapple3.png', 'score': 150})

apple_surface = [pygame.image.load('images/'+data['path']).convert_alpha() for data in apples]

img_apples = pygame.sprite.Group()


def createApple(group):
    indx = randint(0, len(apple_surface)-1)
    x = randint(20, WIDTH-20)
    speed = randint(1, 4)

    return Apple(x, speed, apple_surface[indx], apples[indx]['score'], group)   # обращеамся к классу и возвращаем координата x, скорость, поверхность и кол-во очков и группа из яблок


createApple(img_apples)
speed = 15 #скорость зайца



def  collisionApples():
    global game_score
    for apple in img_apples:
        if t_rect.collidepoint(apple.rect.center):
            game_score += apple.score
            apple.kill()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createApple(img_apples)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > WIDTH-t_rect.width:
            t_rect.x = WIDTH-t_rect.width

    serface.blit(background, (0, 0))
    img_apples.draw(serface)
    serface.blit(score, (0, 0))
    serface_text = font.render(str(game_score), 1, (0, 0, 0))
    serface.blit(serface_text, (30, 10))
    serface.blit(animal, t_rect)
    pygame.display.update()



    img_apples.update(HEIGHT)
    collisionApples()

    counter.tick(FPS)




