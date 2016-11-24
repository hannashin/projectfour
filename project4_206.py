import pygame
import time
import random
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
pygame.display.set_caption('Everyday College')

#Timer
start = time.time()

#text size
pygame.font.init()
text = pygame.font.Font(pygame.font.get_default_font(), 12)
formeonly= False

#Square Screen
width_display = 500
height_display = 500
screen_display = pygame.display.set_mode(width_display,height_display)

pygame.mixer.init()

#Sounds game
music = pygame.mixer.Sound("media/run_song.wav")
weapon = pygame.mixer.Sound("media/ohmygod.wav")
leaving = pygame.mixer.Sound("media/okay_bye.wav")

#Location and Start
#Location
done = False
position = (0,0)
pencil = 0
bn = 0
score = 0

#Avoiding target images
avoid_images = ["data/snowflake.png", "data/eight_thirty.png", "data/homework.png"]

#Game Classes:
class Sprite:
	def __init__(self, image1 = )


#Game positioning and screen starting display



#Ending of game
print ("Student:")
print (student_name)
print ("Score:")
print (score)
print ("Time:")
print(time.time()-start, "\n")
pygame.quit()
ending = None

while ending != "Q":
	ending = input("Press Q to Quit game:")
	if ending == "Q":
		break
print ("FINISHED GAME")
quit 



