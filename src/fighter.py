__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import pygame
import random
import util

from projectile import Projectile

class Fighter(pygame.sprite.Sprite):
    """A fighter plane.

    Attrs:
        SPEED (int): The fighter's speed in pixels per frame.
        PROJECTILE_SPEED (int): The fighter's projectile speed in pixels per
            frame. The fighter's projectiles fire upward on the screen (toward
            the origin), so we assign a negative speed.

    """
    SPEED = 5
    PROJECTILE_SPEED = -5

    # Available fighter colors.
    __COLORS = ['blue','green','orange','red']
    # All fighter image files are in this format. A random fighter color is
    # chosen and loaded when the constructor is called.
    __IMG_FILE_FMT = os.path.join(img_res_dir, 'figher_{color}.png')

    def __init__(self, screen_res):
        """Initialize a fighter plane object.

        Args:
            screen_res ((int,int)): The (w,h) dimensions of the screen.

        Attrs:
            img (pygame.Surface): The fighter's image.
            pos ((int,int)): The (x,y) coords of the fighter's image.
            rect (pygame.Rect): The rectangle that surrounds the fighter's
                image.
            hitbox (pygame.Rect): The area used for collision detection.
            attack (int): The fighter's attack value (used to assign the damage
                value of projectiles).
            defense (int): The fighter's defense value.
            projectiles ([projectile.Projectile]): All of the projectiles that
                the fighter has shot.

        """
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(self.__get_rand_fighter_file())
        self.pos = self.__get_init_pos(screen_res)
        self.rect = self.img.get_rect(topleft=self.pos)
        self.hitbox = None
        self.attack = 1
        self.defense = 1
        self.projectiles = []

    def draw(self, screen):
        """Draw the fighter on the screen at its current position.

        Args:
            screen (pygame.Surface): The screen to display the fighter on.

        """
        screen.blit(self.img, self.pos)

    def move(self, delta, screen_rect):
        """Update the fighter's position if it remains completely on-screen
        after the changes. Otherwise, leave it where it is.

        Args:
            delta ((int,int)): The (x,y) changes in the fighter's position.
            screen_rect (pygame.Rect): The rectangle that borders the game's
                screen.

        """
        potential_pos = self.__get_potential_pos(delta)
        if screen_rect.contains(self.rect):
            self.pos = potential_pos
            # We also have to update the position of the fighter's rectangle.
            potential_rect = self.img.get_rect(topleft=potential_pos)
            self.rect = potential_rect

    def shoot(self):
        """Shoot a projectile. This function creates a projectile and appends
        it to the calling object's projectiles list.

        """
        self.projectiles.append(Projectile(self))

    def __get_rand_fighter_file(self):
        # Obtain a fighter image file with a random color from
        # Fighter.__COLORS.
        return __IMG_FILE_FMT.format(random.choice(__COLORS))

    def __get_init_pos(self, res):
        # Get an initial position for the fighter (the center of the bottom
        # third of the screen).
        (screen_width,screen_height) = res
        (fighter_width,fighter_height) = self.img.get_size()
        # To align the fighter horizontally, find the horizontal center of the
        # screen, and move the fighter n units left, where n is half of its
        # width.
        fighter_x = (screen_width / 2) - (fighter_width / 2)
        # To align the fighter vertically, first find the top of the bottom
        # third of the screen...
        top = int(screen_height * (2 / 3))
        # ...then find the vertical center of this bottom third, and move the
        # fighter n units up, where n is half of its height.
        fighter_y = top + ((screen_height - top) / 2) - (fighter_height / 2)
        return (fighter_x,fighter_y)

    def __get_potential_pos(self, delta):
        # Get the potential new position of the fighter, should the given
        # changes be applied.
        return util.tupadd(self.pos, delta)
