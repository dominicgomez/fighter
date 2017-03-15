__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import pygame

class __Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        """Initialize an enemy object. This constructor should only be called
        by other functions in this module.

        """
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(const.ENEMY_IMG)

def spawn_static(n, ring):
    pass
