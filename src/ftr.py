__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

"""Fighter: A Galaga-inspired shooter game.

This module contains the game's main loop.

"""

import pygame
from pygame.locals import *

import const
from fighter import Fighter
import util

def draw_bg(scr, bg):
    """Draw the game's background.

    Args:
        scr (pygame.Surface): The screen to draw on.
        bg (pygame.Surface): The image to draw.

    """
    # Tile images that aren't big enough to fill the screen.
    (scr_w,scr_h) = scr.get_size()
    (bg_w,bg_h) = bg.get_size()
    for i in range(0, scr_w, bg_w):
        for j in range(0, scr_h, bg_h):
            scr.blit(bg, (i,j))

def draw_ftr(scr, ftr):
    """Draw the fighter.

    Args:
        scr (pygame.Surface): The screen to draw on.
        ftr (fighter.Fighter): The fighter to draw.

    """
    scr.blit(ftr.img, ftr.pos)

def move_projs(projs):
    """Advance the positions of the projectiles on screen."""
    for proj in projs:
        (x,y) = proj.pos
        proj.pos = (x,y-const.PROJ_DELTA)

def draw_projs(scr, projs):
    """Draw the projectiles."""
    for proj in projs:
        scr.blit(proj.img, proj.pos)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    scr = pygame.display.set_mode((const.SCR_W,const.SCR_H))
    bg = pygame.image.load(const.BG_IMG)
    ftr = Fighter(scr.get_size())
    projs = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # You can only shoot once per frame, the key must be pressed
                # down each time.
                if event.key == pygame.K_SPACE:
                    projs.append(ftr.shoot())

        # But why are you pressed tho?
        pressed = pygame.key.get_pressed()
        # Keep track of the total change in direction so we only have
        # to issue one call to move
        (x_delta,y_delta) = (0,0)
        if pressed[pygame.K_LEFT]:
            x_delta -= const.FTR_X_DELTA
        if pressed[pygame.K_UP]:
            y_delta -= const.FTR_Y_DELTA
        if pressed[pygame.K_DOWN]:
            y_delta += const.FTR_Y_DELTA
        if pressed[pygame.K_RIGHT]:
            x_delta += const.FTR_X_DELTA

        # Move the objects on screen
        ftr.move((x_delta,y_delta), scr.get_size())

        # Remove the projectiles that have moved off screen
        projs = [proj for proj in projs if proj.is_on_screen(scr.get_size())]

        clock.tick(const.FRAMERATE)

        # Update the screen.
        draw_bg(scr, bg)
        draw_ftr(scr, ftr)
        draw_projs(scr, projs)
        pygame.display.flip()

        move_projs(projs)

    pygame.quit()

if __name__ == '__main__':
    main()