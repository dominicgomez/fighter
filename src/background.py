__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import pygame

class Background:
    def __init__(self, img):
        """Initialize the game's background.

        """
        self.img = pygame.image.load(img)
