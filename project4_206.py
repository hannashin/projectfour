#Han Na Shin
#SI 206 - Project 4 Pygame


from pygame import *
import time
from pygame.sprite import *
from random import *

print ("""Having a tough day? Well my friend, we're in college. Avoid all the things coming your way! Good luck and Go Blue!""")

student_name = input("What's your name, student?")
if student_name == "":
	name = "Hanna Shin"

#Start of Game --- leaving terminal

pygame.init()

#colors
#Colors
white = (255,255,255)
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)

#Display 
pygame.display.set_caption('Trying to Avoid')

#Timer
timer = pygame.time.Clock()

#text size
pygame.font.init()
text = pygame.font.Font(pygame.font.get_default_font(), 12)

#Square Screen
display_size = display.set_mode((400,600))

pygame.mixer.init()

#Sounds game
music = pygame.mixer.Sound("media/run_song.wav")
weapon = pygame.mixer.Sound("media/ohmygod.wav")
leaving = pygame.mixer.Sound("media/okay_bye.wav")

#Avoiding target images

#Game Classes:
class Snowflake(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("data/snowflake.png").convert_alpha()
        self.rect = self.image.get_rect()

    def placed(self):
    	x_axis = randint(0,300)
    	y_axis = randint(0,150)
    	self.rect.center = (x_axis, y_axis)

class Clocktime(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("data/eight_thirty.png").convert_alpha()
        self.rect = self.image.get_rect()

    def placed(self):
    	x_axis = randint(0,75)
    	y_axis = randint(0,200)
    	self.rect.center = (x_axis, y_axis)

class Homework(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("data/homework.png").convert_alpha()
        self.rect = self.image.get_rect()

    def placed(self):
        x_axis = randint(0,100)
        y_axis = randint(0,100)
        self.rect.center = (x_axis, y_axis)


class Student(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("data/student.png").convert()
		self.rect = self.image.get_rect()

    # def avoided(self, target):
    #     return self.rect.colliderect(target)

    # def update(self):
    #     self.rect.center = mouse.get_pos()


#game code
# mouse.set_visible(False)
# snowflake = Snowflake()
# clocktime = Clocktime()
# homework = Homework()
# student = Student()
# colliders = RenderPlain(snowflake, clocktime, homework, student)

# hits = 0

#while True:







