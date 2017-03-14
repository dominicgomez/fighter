__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import pygame

import const

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        """Initialize a projectile.

        """
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(const.PROJ_IMG)
