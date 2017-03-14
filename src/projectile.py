__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import pygame

import const

class Projectile(pygame.sprite.Sprite):
    def __init__(self, ftr):
        """Initialize a projectile.

        Args:
            ftr (fighter.Fighter): The fighter to shoot from.

        """
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(const.PROJ_IMG)
        self.hitbox = None
        self.pos = self.__get_init_pos(ftr)

    def move(self):
        """Advance the projectile's position."""

    def __get_init_pos(self, ftr):
        (ftr_x,ftr_y) = ftr.pos
        (ftr_w,_) = ftr.img.get_size()
        (proj_w,proj_h) = self.img.get_size()
        proj_x = ftr_x + (ftr_w / 2) - (proj_w / 2)
        proj_y = ftr_y - proj_h
        return (proj_x,proj_y)
