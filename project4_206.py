# Han Na Shins

#Use modules, classes, and event detection
# Movement, Collision Detecion, Scoring and/or time, animation, sound
#Two weeks of commits (10 diff days, 5 hours apart)
#Class inheritance

from pygame import *
from pygame.sprite import *
from random import *

#Timer to move sprite
DELAY = 1000;          

#Colors 
backgroundimage = pygame.image.load("images/campus.jpg")
white = (255,255,255)
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)   



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

    # move gold to a new random location
    def move(self):
        randX = randint(0, 400)
        randY = randint(0, 200)
        self.rect.center = (randX,randY)

class Eightthirty(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/eight_thirty.png").convert_alpha()
        self.rect = self.image.get_rect()

    # move gold to a new random location
    def move(self):
        randX = randint(0, 150)
        randY = randint(100, 150)
        self.rect.center = (randX,randY)

class Student(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("images/student.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black) #makes it transparent

    # Di shovel/cursor collide the gold?
    def hit(self, target):
        return self.rect.colliderect(target)

    #The shovel sprite will move with the mousepointer
    def update(self):
        self.rect.center = mouse.get_pos()

    def movement(self, moving, running):
        x = 10
        if running == START:
            if moving in (UP, DOWN):
                self.dy = {UP: -x, DOWN: x} [moving]

            if moving in (LEFT, RIGHT):
                self.dx = {LEFT: -x, RIGHT: x} [moving]

            if running == STOP:
                if moving in (UP, DOWN):
                    self.dy = 0
                if moving in (LEFT, RIGHT):
                    self.dx = 0

class PencilBullet(Sprite):
    def __init__(self):
        Sprite.__init__(self, 'images/pencil.png')
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

finished_game = False

#background music infinite loop
pygame.mixer.music.load("songs/run_song.wav")
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
    for event in pygame.event.get():
        if event.type == QUIT:
            finished_game = True

        if not finished_game:
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    student.movement(DOWN,START)
                if event.key == K_LEFT:
                    student.movement(LEFT,START)
                if event.key == K_RIGHT:
                    student.movement(RIGHT,START)




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



