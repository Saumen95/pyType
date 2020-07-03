import pygame
import sys
import random
import time


class Game(object):
    """docstring forGame."""

    def __init__(self):
        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''


        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))
