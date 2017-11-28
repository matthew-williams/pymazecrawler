#!/usr/bin/env python3
# Title:    Python Google Chrome to Chromium migration script
# Author:   Matthew Williams
# Date:     11/21/2017
import subprocess
import os
import sys
import pygame
#
# VARIABLE DEFINITION
#
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((800,600))
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
dead = False
x =  (display_width * 0.45)
y = (display_height * 0.8)
#
# END OF VARIABLE DEFINITION
#
#
# FUNCTIONS DEFINITION
#
#
# END OF FUNCTIONS DEFINITION
#

#
# PROGRAM DEFINITION
#

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Maze')
charImg = pygame.image.load('character.jpg')

def char(x,y):
    gameDisplay.blit(charImg, (x,y))

while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        print(event)
    gameDisplay.fill(white)
    char(x,y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
#
# END OF PROGRAM DEFINITION
#
