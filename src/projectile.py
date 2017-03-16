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
        self.pos = self.__get_init_pos(ftr)
        self.hitbox = self.img.get_rect(topleft=self.pos)
        self.collided = False

    def move(self):
        """Advance the projectile's position."""

    def is_on_screen(self, res):
        """Determine if any part of the projectile is still on screen."""
        (x,y) = self.pos
        return y > -self.img.get_height()

    def __get_init_pos(self, ftr):
        (ftr_x,ftr_y) = ftr.pos
        (ftr_w,_) = ftr.img.get_size()
        (proj_w,proj_h) = self.img.get_size()
        proj_x = ftr_x + (ftr_w / 2) - (proj_w / 2)
        proj_y = ftr_y - proj_h
        return (proj_x,proj_y)
