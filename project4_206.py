from pygame import *
from pygame.sprite import *
from random import *


#Timer to move sprite
DELAY = 1200; #speed of the targets          

#Colors 
backgroundimage = pygame.image.load("images/campus.jpg")
white = (255,255,255)
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)   


#Avoiding Image Classes
class Snowflake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/snowflake.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 400)
        self.rect.center = (randX,randY)

class Homework(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/homework.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 400)
        randY = randint(0, 200)
        self.rect.center = (randX,randY)

class Eightthirty(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/eight_thirty.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 150)
        randY = randint(100, 150)
        self.rect.center = (randX,randY)

#Target Image Classes
class Coffee(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/coffee.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 300)
        randY = randint(0, 116)
        self.rect.center = (randX,randY)


class APlus(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/aplus.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 222)
        randY = randint(0, 222)
        self.rect.center = (randX, randY)

#Student class
class Student(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/student.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black) #makes it transparent

    def hit(self, target):
        return self.rect.colliderect(target)

    def update(self):
        self.rect.center = pygame.mouse.get_pos() #should follow mouse around


#---------prints in terminal befoer game starts------------
print ("""Your goal is to hit all of the daily tasks as college students we are trying to avoid. Have fun!""")

student_name = input("What's your name, student?:")
if student_name == "":
    name = "Hanna Shin"

#main
pygame.init()

#background music infinite loop
pygame.mixer.music.load("songs/run_song.wav")
pygame.mixer.music.play(-1)

screen = display.set_mode((800, 640))
display.set_caption('College Student Daily Tasks')

pygame.mouse.set_visible(False)

f = font.Font(None, 18)

# constructions of the avoiding images
snowflake = Snowflake()
homework = Homework()
eightthirty = Eightthirty()
student = Student()

#constructions of the target images
coffee = Coffee()
aplus = APlus()

# creates a group of sprites so all can be updated at once
sprites = RenderPlain(snowflake, student)
sprites1 = RenderPlain(homework, student)
sprites2 = RenderPlain(eightthirty, student)
sprites3 = RenderPlain(coffee, student)
sprites4 = RenderPlain(aplus, student)

hits = 0
timer_zone = time.set_timer(USEREVENT + 1, DELAY)

#clock
clock = pygame.time.Clock()

# loop until user quits
while True:
    clock.tick(30)
    x = event.poll()
    student.update()
    if x.type == QUIT:
        quit()
        break

    elif x.type == MOUSEMOTION:
        
        if student.hit(snowflake):
            snowflake.move()
            hits += 0

        if student.hit(homework):
            homework.move()
            hits += 0

        if student.hit(eightthirty):
            eightthirty.move()
            hits += 0

        if student.hit(coffee):
            coffee.move()
            hits += 0        

        if student.hit(aplus):
            aplus.move()
            hits += 0

    elif x.type == MOUSEBUTTONDOWN:

        if student.hit(snowflake):
            mixer.Sound("songs/ohmygod.wav").play()
            snowflake.move()
            hits -= 1 

        if student.hit(homework):
            mixer.Sound("songs/okay_bye.wav").play()
            homework.move()
            hits -= 1

        if student.hit(eightthirty):
            mixer.Sound("songs/okay_bye.wav").play()
            eightthirty.move()
            hits -= 1

        if student.hit(coffee):
            mixer.Sound('songs/woohoo.wav').play()
            coffee.move()
            hits += 1

        if student.hit(aplus):
            mixer.Sound('songs/woohoo.wav').play()
            aplus.move()
            hits += 1

            # reset timer
            time.set_timer(USEREVENT + 1, DELAY)
            
    elif x.type == USEREVENT:
        snowflake.move()
        homework.move()
        eightthirty.move()
        coffee.move()
        aplus.move()

    # refill background color so that we can paint sprites in new locations
    screen.blit(backgroundimage, [0,0])
    t = f.render("Stuck with:" + str(hits), False, (255,255,255))
    y = f.render("Time: = " + str(clock), True, (255,255,255))
    z = f.render('Student:' + str(student_name), False, (255,255,255))
    screen.blit(z, (0, 0))
    screen.blit(t, (0, 20)) 
    screen.blit(y, (0, 40))
         

    # update and redraw sprites
    sprites.update()
    sprites1.update()
    sprites2.update()
    sprites3.update()
    sprites4.update()
    sprites.draw(screen)
    sprites1.draw(screen)
    sprites2.draw(screen)
    sprites3.draw(screen)
    sprites4.draw(screen)
    display.update()

#----------END OF TERMINAL SHOWING SCORES WHEN GAME QUIT-------

print ("------------------------------------------")
print (str(student_name) + ", you avoided a lot of daily tasks!")
print ('You avoided ' + str(hits) + ' tasks!')
print ('END OF GAME - GET BACK TO WORK!')
