__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import dirs
import os
import pygame

class Projectile(pygame.sprite.Sprite):

    # The possible types of projectiles.
    __TYPES = ['fighter','enemy']
    # All projectile image files are in this format. The appropriate projectile
    # type is chosen from __TYPES, based on the projectile's speed, and loaded
    # when the constructor is called.
    __IMG_FILE_FMT = os.path.join(dirs.IMG_RES_DIR, 'proj_{type}.png')

    def __init__(self, shooter_rect, speed, dmg):
        """Initialize a projectile.

        Args:
            shooter_rect (pygame.Rect): The rectangle surrounding the image of
                the object that shot the projectile.
            speed (int): The speed that the projectile should move, in pixels
                per frame. If this value is positive, the projectile moves down
                on the screen (shot by enemy); if it is negative, the
                projectile moves up on the screen (shot by fighter).
            dmg (int): The amount of damage that the projectile deals when it
                collides. This value should be the same as the origin's attack
                value.

        Attrs:
            alive (bool): Whether the enemy is alive. The game should set this
                flag to False when it detects a collision involving this enemy.
            img (pygame.Surface): The enemy's image.
            pos ((int,int)): The (x,y) coords of the enemy's image.
            rect (pygame.Rect): The rectangle that surrounds the enemy's image.
            hitbox (pygame.Rect): The area used for collision detection.
            speed (int): The projectile's speed in pixels per frame.
            dmg (int): The amount of damage that the projectile deals when it
                collides.

        """
        pygame.sprite.Sprite.__init__(self)

        self.alive = True
        self.img = (
            self.__get_proj_file('enemy') if speed > 0
            else self.__get_proj_file('fighter')
        )
        self.pos = self.__get_init_pos(shooter_rect)
        self.rect = self.img.get_rect(topleft=self.pos)
        self.hitbox = self.rect
        self.dmg = dmg

    def move(self, screen_rect):
        """Advance the projectile's position."""

    def is_on_screen(self, res):
        """Determine if any part of the projectile is still on screen."""
        (x,y) = self.pos
        return y > -self.img.get_height()

    def __get_proj_file(self, type):
        return __IMG_FILE_FMT.format(type=type)

    def __get_init_pos(self, ftr):
        (ftr_x,ftr_y) = ftr.pos
        (ftr_w,_) = ftr.img.get_size()
        (proj_w,proj_h) = self.img.get_size()
        proj_x = ftr_x + (ftr_w / 2) - (proj_w / 2)
        proj_y = ftr_y - proj_h
        return (proj_x,proj_y)
