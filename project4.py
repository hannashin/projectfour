import pygame
import time
import random

pygame.init()

#Square Screen
width_display = 500
height_display = 500

#Colors
white = (255,255,255)
black = (0,0,0)
red = (200, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)

#anchor person
width_student = 25
height_student = 80

#Sound
student_sound = pygame.mixer.Sound("bloop.wav") #collision sound
pygame.mixer.music.load("classbell.wav") #Sound throughout the game

#Game Display
display_game = pygame.display.set_mode((width_display, height_display))
pygame.display.set_caption("Just in College")

#Scoring and or Time
time = pygame.time.Clock()

#Student image
student_img = pygame.image.load("student_run.gif")
#logogame = pygame.image.load("PICTUREOFWHATEVER.png") #or .jpeg

#Game
pause = False

def quitgame():
    pygame.quit()
    quit() #Quits the game

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()


def main():

#Animation

#Movement