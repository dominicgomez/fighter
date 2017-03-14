__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import pygame

import const
from projectile import Projectile
import util

class Fighter(pygame.sprite.Sprite):
    def __init__(self, res):
        """Initialize a fighter object.

        Args:
            res ((int,int)): The (w,h) dimensions of the screen.

        Attrs:
            img (pygame.Surface): The fighter's image.
            hitbox (pygame.Rect): The area used for collision detection.
            pos ((int,int)): The (x,y) coords of the fighter's image.
            attack (int): The fighter's attack value.
            defense (int): The fighter's defense value.

        """
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(const.FTR_IMG)
        self.hitbox = None
        self.pos = self.__get_init_pos(res)
        self.attack = 1
        self.defense = 1

    def move(self, delta, res):
        """Update the fighter's position if its entire image remains on screen.

        Args:
            delta ((int,int)): The (x,y) changes in the fighter's position.
            res ((int,int)): The (w,h) dimensions of the screen.

        """
        pos = self.__get_new_pos(delta)
        if self.__is_in_bounds(pos, res):
            self.pos = pos

    def shoot(self, scr):
        """Shoot a projectile.

        """
        proj = Projectile()
        scr.blit(proj.img, (self.pos[0]+self.img.get_width()/2,self.pos[1]))

    def __get_init_pos(self, res):
        """Get an initial position for the fighter (the center of the bottom
        third of the screen).

        Args:
            res ((int,int)): The (w,h) dimensions of the screen.

        Return:
            ((int,int)): The (x,y) coords of the fighter.

        """
        (scr_w,scr_h) = res
        (ftr_w,ftr_h) = self.img.get_size()
        # To align the fighter horizontally, find the horizontal center of the
        # screen, and move the fighter n units left, where n is half of its
        # width.
        x = (scr_w / 2) - (ftr_w / 2)
        # To align the fighter vertically, first find the top of the bottom
        # third of the screen...
        top = scr_h / 3 * 2
        # ...then find the vertical center of this bottom third, and move the
        # fighter n units up, where n is half of its height.
        y = top + ((scr_h - top) / 2) - (ftr_h / 2)
        return (x,y)

    def __get_new_pos(self, delta):
        """Get the new position of the fighter, should the given changes be
        applied.

        Args:
            delta ((int,int)): The (x,y) changes in the fighter's position.

        """
        return util.tupadd(self.pos, delta)

    def __is_in_bounds(self, pos, res):
        """Determine whether the fighter would be completely visible at the
        given position.

        Args:
            pos ((int,int)): The (x,y) coords of the new potential location.
            res ((int,int)): The (w,h) dimensions of the screen.

        """
        (x,y) = pos
        (scr_w,scr_h) = res
        (ftr_w,ftr_h) = self.img.get_size()
        # Make sure it's not too high or too far left.
        if x < 0 or y < 0: return False
        # Make sure it's not too low or too far right.
        if x > (scr_w - ftr_w) or y > (scr_h - ftr_h): return False
        return True
