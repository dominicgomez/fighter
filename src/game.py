__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import os
import pygame
from pygame.locals import *

import conf
from enemy import Enemy
from fighter import Fighter
from player import Player
import util

class Game:
    """The game machine.

    Attrs:
        NAME (str): The game's name.
        VERSION (str): The game's version.

        SCREEN_LAYOUTS ([str]): Identifiers for available display layouts.
        TITLE_MENU_OPTIONS ([str]): The options on the game's title screen.
        PLAY_MODES ([str]): The available play modes. The different modes
            change how the enemies act against the fighter.

    """
    NAME = 'Fighter'
    VERSION = None

    SCREEN_LAYOUTS = ['title','play','high scores','settings']
    TITLE_MENU_OPTIONS = ['play','high scores','settings']
    PLAY_MODES = ['standard','survival']

    def __init__(self):
        """Initialize the game machine. (This constructor does not start a
        game.)

        Attrs:
            SCREEN_RES ((int,int)): The screen resolution.
            BG (pygame.Surface): The game's background.

            clock (pygame.time.Clock):
            screen (pygame.Surface): The game's screen.
            player (player.Player):
            fighter (fighter.Fighter):
            enemies ([enemy.Enemy]):
            projectiles ([projectile.Projectile]):

        """
        self.SCREEN_RES = conf.SCREEN_RES
        self.BG = pygame.image.load(conf.bg_img_file)

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_res)
        # The player, fighter, enemies, and projectiles are not instantiated
        # until they need to be.
        self.player = None
        self.fighter = None
        self.enemies = []
        self.projectiles = []

        self.__draw_screen()

    def __draw_screen(self, screen_layout):
        # Draw everything on the screen in the right order.
        self.__draw_background()
        if screen_layout == 'title':
            self.__display_title_screen()
        elif screen_layout == 'play':
            pass
        elif screen_layout == 'high scores':
            pass
        elif screen_layout == 'settings':
            pass
        else:
            raise RuntimeError('Invalid screen layout')

    def __draw_background(self):
        # Draw the background on the screen.
        background.draw(self.screen, self.bg)

    def __display_title_screen(self):
        # Display the game's title screen.
        title_font = pygame.font.Font(
            filename = conf.title_font_file,
            size = conf.title_font_size
        )
        title_label = title_font.render(
            text = title,
            antialias = True,
            color = (0,0,0)
        )
        title_pos = self.__get_title_pos(screen)

    def __get_title_pos(self):
        # Get the position of the title text on the screen, which should be in
        # the center of the top third of the screen.
        # Get a rectangle the size of the top third of the screen.
        rect = pygame.Rect

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
        # Move their hitboxes
        proj.hitbox = proj.img.get_rect(topleft=proj.pos)

def draw_projs(scr, projs):
    """Draw the projectiles."""
    for proj in projs:
        scr.blit(proj.img, proj.pos)

def draw_enemies(scr, enemies):
    """Draw the enemies."""
    for enemy in enemies:
        scr.blit(enemy.img, enemy.pos)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    scr = pygame.display.set_mode((const.SCR_W,const.SCR_H))
    rect = scr.get_rect()
    bg = pygame.image.load(const.BG_IMG)
    ftr = Fighter(scr.get_size())
    projs = []
    enemies = []

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

        if not enemies:
            enemies.append(Enemy(scr.get_size()))

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
        draw_enemies(scr, enemies)

        move_projs(projs)

        # Collision detection
        enemies = [e for e in enemies if not e.has_been_popped(projs)]
        projs = [proj for proj in projs if not proj.collided]

        pygame.display.flip()


    pygame.quit()

if __name__ == '__main__':
    main()
