import sys
import random
import math
import pygame
from pygame.locals import *
from classes import Asteroid

def terminate():
    pygame.quit()
    sys.exit()


def draw_text(text, font, surface, x, y, TEXTCOLOR):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect(center=(x // 2, y // 2 ))
    surface.blit(textobj, textrect)


def wait():

    waiting = True    
    
    while waiting:
        
        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                waiting = False


def generate_asteroid(window):
    direction = random.uniform(0, 2 * math.pi)
    direction = random.uniform(0, 2 * math.pi)
    start_x = window.width / 2 + math.cos(direction) * window.width
    start_y = window.height / 2 + math.sin(direction) * window.height
    target_x = window.width / 2
    target_y = window.height / 2
    speed = random.randint(3, 5)
    dx = target_x - start_x
    dy = target_y - start_y
    size = random.randint(5, 10)
    angle = math.degrees(math.atan2(dy, dx))
    return Asteroid(start_x, start_y, target_x, target_y, angle, speed, size)