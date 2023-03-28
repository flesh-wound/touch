import pygame, sys
from pygame.locals import *
pygame.init()
pygame.font.init()
fontfont = pygame.font.SysFont('Comic Sans MS', 30)
touch_font = pygame.font.SysFont('Comic Sans MS', 60)
rules_font = pygame.font.SysFont('Comic Sans MS', 25)
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
background = (66,126,96)
rect_color = (53,101,77)
 
#Other Variables for use in the program
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 804

#Create a white screen 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill(background)
pygame.display.set_caption("TOUCH!")