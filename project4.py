from pygame import *
from pygame.sprite import *
from random import *

#Timer to move sprite
DELAY = 1400; #speed of movement of the targets

#Colors 
backgroundimage = pygame.image.load("images/campus.jpg")
white = (255,255,255)
black = (0,0,0)
 


#-----IMAGES TO AVOID-----
class Snowflake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/snowflake.png").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
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
        randX = randint(0, 600)
        randY = randint(0, 600)
        self.rect.center = (randX,randY)

class Eightthirty(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/eight_thirty.png").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 600)
        randY = randint(100, 600)
        self.rect.center = (randX,randY)

#------IMAGES TO NOT AVOID-----
class Coffee(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/coffee.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 600)
        self.rect.center = (randX,randY)

class Aplus(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/aplus.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 600)
        randY = randint(0, 600)
        self.rect.center = (randX,randY)

class Friends(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/friends.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 550)
        randY = randint(0, 600)
        self.rect.center = (randX,randY)

class Art(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/art.png").convert_alpha()
        self.rect = self.image.get_rect()

    def move(self):
        randX = randint(0, 550)
        randY = randint(0, 550)
        self.rect.center = (randX,randY)

#-----STUDENT IMAGE ------
class Student(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/student.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black) #makes student transparent

    def hit(self, target):
        return self.rect.colliderect(target)

    def update(self):
        self.rect.center = pygame.mouse.get_pos() 

#---------prints in terminal befoer game starts------------
print ("""STUDENT BOOST PACK GAME : Your goal is to click on the daily tasks to get boost points as the student (images such as firends, coffee, and an A+!) Try to avoid the snowflake, books, and 8:30 AM clock if you don't want to lose points! Click the screen to get the game started. Have fun!""")

student_name = input("What's your name, student?:")
if student_name == "":
    name = "Hanna Shin"

#main
pygame.init()

#background music infinite loop
pygame.mixer.music.load("songs/run_song.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)

screen = display.set_mode((800, 640))
display.set_caption('Student Boost Pack')

pygame.mouse.set_visible(False)

f = font.Font(None, 24)

# constructions of the enemy images
snowflake = Snowflake()
homework = Homework()
eightthirty = Eightthirty()
student = Student()
coffee = Coffee()
aplus = Aplus()
friend = Friends()
art = Art()

# creates a group of sprites so all can be updated at once
sprites = RenderPlain(snowflake, student)
sprites1 = RenderPlain(homework, student)
sprites2 = RenderPlain(eightthirty, student)
sprites3 = RenderPlain(coffee, student)
sprites4 = RenderPlain (aplus, student)
sprites5 = RenderPlain (friend, student)
sprites6 = RenderPlain (art, student)

hits = 0
timer_zone = time.set_timer(USEREVENT + 1, DELAY)

while True:
    x = event.poll()
    student.update()
    if x.type == QUIT:
        quit()
        break

    elif x.type == MOUSEMOTION:
        #
        if student.hit(snowflake):
            snowflake.move()
            hits += 0

        if student.hit(homework):
            snowflake.move()
            hits += 0

        if student.hit(eightthirty):
            snowflake.move()
            hits += 0

        if student.hit(coffee):
            coffee.move()
            hits += 0   

        if student.hit(aplus):
            aplus.move()
            hits += 0

        if student.hit(friend):
            friend.move()
            hits += 0

        if student.hit(art):
            art.move()
            hits += 0         

    elif x.type == MOUSEBUTTONDOWN:
        if student.hit(snowflake):
            mixer.Sound("songs/ohmygod.wav").play()
            snowflake.move()
            hits -= 1

        if student.hit(homework):
            mixer.Sound("songs/ohmygod.wav").play()
            homework.move()
            hits -= 1

        if student.hit(eightthirty):
            mixer.Sound("songs/ohmygod.wav").play()
            eightthirty.move()
            hits -= 1

        if student.hit(coffee):
            mixer.Sound("songs/woohoo.wav").play()
            coffee.move()
            hits += 1

        if student.hit(aplus):
            mixer.Sound("songs/woohoo.wav").play()
            aplus.move()
            hits += 1

        if student.hit(friend):
            mixer.Sound("songs/woohoo.wav").play()
            friend.move()
            hits += 1

        if student.hit(art):
            mixer.Sound("songs/woohoo.wav").play()
            art.move()
            hits += 1

            time.set_timer(USEREVENT + 1, DELAY)
            
    elif x.type == USEREVENT + 1: # TIME has passed
        snowflake.move()
        homework.move()
        eightthirty.move()
        coffee.move()
        aplus.move()
        friend.move()
        art.move()

    # refill background color so that we can paint sprites in new locations
    screen.blit(backgroundimage, [0,0])
    t = f.render("Boost Pack:" + str(hits), False, (255,255,255))
    z = f.render('Student Name:' + str(student_name), False, (255,255,255))
    screen.blit(z, (10, 10))
    screen.blit(t, (10, 50))
         
    # update and redraw sprites for game 
    sprites.update()
    sprites1.update()
    sprites2.update()
    sprites3.update()
    sprites4.update()
    sprites5.update()
    sprites6.update()
    sprites.draw(screen)
    sprites1.draw(screen)
    sprites2.draw(screen)
    sprites3.draw(screen)
    sprites4.draw(screen)
    sprites5.draw(screen)
    sprites6.draw(screen)
    display.update()

#----------END OF TERMINAL SHOWING SCORES WHEN GAME QUIT-------

print ("------------------------------------------")
print (str(student_name) + ", this is your boost pack score for the day!")
print ('You got ' + str(hits) + ' boost pack points!')
print ('END OF GAME - GET BACK TO WORK!')