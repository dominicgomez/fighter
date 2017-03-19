__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import dirs
import os
import pygame
import random

class Enemy(pygame.sprite.Sprite):
    """An enemy."""

    # The enemy's (inclusive) range of speeds, randomly generated when an
    # object is constructed.
    __SPEED_RNG = (0,10)
    # The enemy's (inclusive) range of projectile speeds, randomly generated
    # when an enemy shoots a projectile.
    __PROJECTILE_SPEED_RNG = (0,10)
    # Available enemy colors.
    __COLORS = ['black','blue','green','red']
    # All enemy image files are in this format. A random enemy color is chosen
    # and loaded when the constructor is called.
    __IMG_FILE_FMT = os.path.join(dirs.IMG_RES_DIR, 'enemy_{color}.png')

    def __init__(self, screen_res):
        """Initialize an enemy object.

        Args:
            screen_res ((int,int)): The (w,h) dimensions of the screen.

        Attrs:
            alive (bool): Whether the enemy is alive. The game should set this
                flag to False when it detects a collision involving this enemy.
            img (pygame.Surface): The enemy's image.
            pos ((int,int)): The (x,y) coords of the enemy's image.
            rect (pygame.Rect): The rectangle that surrounds the enemy's image.
            hitbox (pygame.Rect): The area used for collision detection.
            attack (int): The enemy's attack value.
            defense (int): The enemy's defense value.
            projectiles ([projectile.Projectile]): All of the projectiles that
                the enemy has shot.

        """
        pygame.sprite.Sprite.__init__(self)

        self.alive = True
        self.img = pygame.image.load(self.__get_rand_enemy_file())
        self.pos = self.__get_rand_pos(screen_res)
        self.rect = self.img.get_rect(topleft=self.pos)
        self.hitbox = self.rect
        self.attack = 1
        self.defense = 1
        self.projectiles = []

    def __get_rand_enemy_file(self):
        # Obtain an enemy image file with a random color from Enemy.__COLORS.
        return __IMG_FILE_FMT.format(color=random.choice(__COLORS))

    def __get_init_pos(self, screen_res):
        pass

    def __get_rand_pos(self, res):
        (scr_w,scr_h) = res
        (enemy_w,enemy_h) = self.img.get_size()
        x = random.randint(0, scr_w-enemy_w)
        y = random.randint(0, int((scr_h*(2/3)))-enemy_h)
        return (x,y)
