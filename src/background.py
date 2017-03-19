__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

"""This module contains functions to draw and manipulate the game's
background."""

import pygame

def draw(screen, bg):
    """Draw the game's background.

    Args:
        screen (pygame.Surface): The screen to draw on.
        bg (pygame.Surface): The image to draw.

    """
    # Tile images that aren't big enough to fill the screen.
    (screen_width,screen_height) = scr.get_size()
    (bg_width,bg_height) = bg.get_size()
    for i in range(0, screen_width, bg_width):
        for j in range(0, screen_height, bg_height):
            screen.blit(bg, (i,j))

