# Han Na Shinst

from pygame import *
from pygame.sprite import *
from random import *

#Timer to move sprite
DELAY = 1000;          

#Colors 
backgroundimage = pygame.image.load("media/campus.jpg")
white = (255,255,255)
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)   



class Snowflake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("media/snowflake.png").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)

class Homework(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("media/homework.png").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 400)
        randY = randint(0, 200)
        self.rect.center = (randX,randY)

class Eightthirty(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("media/eight_thirty.png").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 150)
        randY = randint(100, 150)
        self.rect.center = (randX,randY)

class Student(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("media/student.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black) #makes it transparent

    # Di shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target)

    #The shovel sprite will move with the mousepointer
    def update(self):
        self.rect.center = mouse.get_pos()

class PencilBullet(Sprite):
    def __init__(self):
        Sprite.__init__(self, 'media/pencil.png')
        self.image=pygame.transform.scale(self.image,(8,12))
        self.width = 8
        self.height = 12
        self.bullet = True
        laser.play()

#---------prints in terminal befoer game starts------------
print ("""Your goal is to hit all of the daily tasks as college students we are trying to avoid. Have fun!""")

student_name = input("What's your name, student?:")
if student_name == "":
    name = "Hanna Shin"

#main
pygame.init()

#background music infinite loop
pygame.mixer.music.load("media/run_song.wav")
pygame.mixer.music.play(-1)

screen = display.set_mode((640, 480))
display.set_caption('College Student Daily Struggles')

# hide the mouse cursor so we only see shovel
mouse.set_visible(False)

f = font.Font(None, 18)

# constructions of the enemy images
snowflake = Snowflake()
homework = Homework()
eightthirty = Eightthirty()
student = Student()

# creates a group of sprites so all can be updated at once
sprites = RenderPlain(snowflake, student)
sprites1 = RenderPlain(homework, student)
sprites2 = RenderPlain(eightthirty, student)

hits = 0
timer_zone = time.set_timer(USEREVENT + 1, DELAY)

#clock
clock = pygame.time.Clock()

# loop until user quits
while True:
    e = event.poll()
    if e.type == QUIT:
        quit()
        break

    elif e.type == MOUSEBUTTONDOWN:
        if student.hit(snowflake):
            mixer.Sound("media/ohmygod.wav").play()
            snowflake.move()
            hits += 1

        if student.hit(homework):
            mixer.Sound("media/okay_bye.wav").play()
            homework.move()
            hits += 1

        if student.hit(eightthirty):
            mixer.Sound("media/okay_bye.wav").play()
            eightthirty.move()
            hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
    elif e.type == USEREVENT + 1: # TIME has passed
        snowflake.move()
        homework.move()
        eightthirty.move()

    # refill background color so that we can paint sprites in new locations
    screen.blit(backgroundimage, [0,0])
    t = f.render("Stuck with:" + str(hits), False, (255,255,255))
    y = f.render("Time: = " + str(clock), False, (255,255,255))
    z = f.render('Student:' + str(student_name), False, (255,255,255))
    screen.blit(z, (0, 0))
    screen.blit(t, (0, 20)) 
    screen.blit(y, (0, 40))
         

    # update and redraw sprites
    sprites.update()
    sprites1.update()
    sprites2.update()
    sprites.draw(screen)
    sprites1.draw(screen)
    sprites2.draw(screen)
    display.update()
    clock.tick(60)

#----------END OF TERMINAL SHOWING SCORES WHEN GAME QUIT-------

print (str(student_name) + ", you avoided a lot of daily struggles!")
print ('You avoided ' + str(hits) + ' tasks!')
print ('END OF GAME - GET BACK TO WORK!')
