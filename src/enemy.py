__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import pygame
import random

import const

class Enemy(pygame.sprite.Sprite):
    def __init__(self, res, pos=None):
        """Initialize an enemy object.

        Args:
            res ((int,int)): The (w,h) dimensions of the screen.
            pos ((int,int)): The position of the enemy. If this value is None,
                a random position is generated for the enemy.

        Attrs:
            img (pygame.Surface): The enemy's image.
            hitbox (pygame.Rect): The area used for collision detection.
            pos ((int,int)): The (x,y) coords of the enemy's image.
            attack (int): The enemy's attack value.
            defense (int): The enemy's defense value.

        """
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(const.ENEMY_IMG)
        self.pos = self.__get_rand_pos(res) if pos is None else pos
        self.hitbox = self.img.get_rect(topleft=self.pos)
        self.attack = 1
        self.defense = 1

    def __get_rand_pos(self, res):
        (scr_w,scr_h) = res
        (enemy_w,enemy_h) = self.img.get_size()
        x = random.randint(0, scr_w-enemy_w)
        y = random.randint(0, int((scr_h*(2/3)))-enemy_h)
        return (x,y)
