__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import dirs
import os
import pygame
import util
from enemy import Enemy
from fighter import Fighter
from pygame.locals import *

class TitleScene:
    # The options to choose from.
    __OPTIONS = ['play','high scores','settings']

    def draw(self, screen):
        options_pos = self.__draw_title(screen)
        self.__draw_options(screen, options_pos)

    def update(self):
        pass

    def handle_event(self, event, keys):
        pass

    def __draw_title(self, screen):
        title_font = pygame.font.Font(Game.TITLE_FONT_FILE,
                                      Game.TITLE_FONT_SIZE)
        title_label = title_font.render(Game.NAME, True, (0,0,0))
        title_pos = self.__center_title(screen.get_rect(),
                                        title_label.get_rect())
        screen.blit(title_label, title_pos)
        return title_label.get_rect(topleft=title_pos).bottomleft

    def __center_title(self, screen_rect, title_rect):
        # Get the center of the screen, and offset the title appropriately.
        x = screen_rect.centerx - int(title_rect.width / 2)
        y = screen_rect.centery - int(title_rect.height / 2)
        return (x,y)

    def __draw_options(self, screen, options_pos):
        font = pygame.font.Font(Game.FONT_FILE, Game.FONT_SIZE)
        option_labels = []
        for option in TitleScene.__OPTIONS:
            option_labels.append(font.render(option, True, (0,0,0)))
        for option_label in option_labels:
            screen.blit(option_label, options_pos)
            options_pos = (options_pos[0],options_pos[1]+option_label.get_height())

class PlayScene:
    def draw(self, screen):
        pass

    def update(self):
        pass

    def handle_event(self, event, keys):
        pass

class HighScoresScene:
    def draw(self, screen):
        pass

    def update(self):
        pass

    def handle_event(self, event, keys):
        pass

class SettingsScene:
    def draw(self, screen):
        pass

    def update(self):
        pass

    def handle_event(self, event, keys):
        pass

class Game:
    """The game machine.

    Attrs:
        NAME (str): The game's name.
        VERSION (str): The game's version.

    """
    NAME = 'Fighter'
    VERSION = None

    # This constant should only be used to initialize the game screen. The
    # screen resolution can be obtained from the game's screen object
    # thereafter.
    __SCREEN_RES = (600,800)
    # A path to the game's background image file.
    __BG_IMG_FILE = os.path.join(dirs.IMG_RES_DIR, 'bg_solid_purple.png')
    # The size of the font used for the game's title.
    TITLE_FONT_SIZE = 100
    # A path to the font used for the game's title.
    TITLE_FONT_FILE = os.path.join(dirs.FONT_RES_DIR, 'title_font.ttf')
    # The size of the font used for all other text in the game.
    FONT_SIZE = 32
    # A path to the font used for all other text in the game.
    FONT_FILE = os.path.join(dirs.FONT_RES_DIR, 'font.ttf')
    # The game's scenes.
    __SCENES = {
        'title' : TitleScene(),
        'play' : PlayScene(),
        'high scores' : HighScoresScene(),
        'settings' : SettingsScene()
    }

    def __init__(self):
        """Initialize the game machine. (This constructor does not start a
        game.)

        Attrs:
            clock (pygame.time.Clock):
            screen (pygame.Surface): The game's screen.
            bg (pygame.Surface): The game's background.
            scene (type): The game's current scene (from __SCENES).

        """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(Game.__SCREEN_RES)
        self.bg = pygame.image.load(Game.__BG_IMG_FILE)
        self.scene = Game.__SCENES['title']
        # self.scene = Game.__SCENES['play']

    def update(self):
        self.__draw_bg()
        self.__draw_title_screen()

    def draw_bg(self):
        # Draw the game's background. Tile images that aren't big enough to
        # fill the screen.
        (screen_width,screen_height) = self.screen.get_size()
        (bg_width,bg_height) = self.bg.get_size()
        for i in range(0, screen_width, bg_width):
            for j in range(0, screen_height, bg_height):
                self.screen.blit(self.bg, (i,j))

# def move_projs(projs):
#     """Advance the positions of the projectiles on screen."""
#     for proj in projs:
#         (x,y) = proj.pos
#         proj.pos = (x,y-const.PROJ_DELTA)
#         # Move their hitboxes
#         proj.hitbox = proj.img.get_rect(topleft=proj.pos)

# def draw_projs(scr, projs):
#     """Draw the projectiles."""
#     for proj in projs:
#         scr.blit(proj.img, proj.pos)

# def draw_enemies(scr, enemies):
#     """Draw the enemies."""
#     for enemy in enemies:
#         scr.blit(enemy.img, enemy.pos)

def main():
    game = Game()
    running = True
    while running:
        game.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                keys = pygame.key.get_pressed()
                game.scene.handle_event(event, keys)
                game.scene.update()
                game.draw_bg()
                game.scene.draw(game.screen)
                pygame.display.flip()
    pygame.quit()

        # # But why are you pressed tho?
        # pressed = pygame.key.get_pressed()
        # # Keep track of the total change in direction so we only have
        # # to issue one call to move
        # (x_delta,y_delta) = (0,0)
        # if pressed[pygame.K_LEFT]:
        #     x_delta -= const.FTR_X_DELTA
        # if pressed[pygame.K_UP]:
        #     y_delta -= const.FTR_Y_DELTA
        # if pressed[pygame.K_DOWN]:
        #     y_delta += const.FTR_Y_DELTA
        # if pressed[pygame.K_RIGHT]:
        #     x_delta += const.FTR_X_DELTA

        # # Move the objects on screen
        # ftr.move((x_delta,y_delta), scr.get_size())

        # # Remove the projectiles that have moved off screen
        # projs = [proj for proj in projs if proj.is_on_screen(scr.get_size())]

        # clock.tick(const.FRAMERATE)

        # # Update the screen.
        # draw_bg(scr, bg)
        # draw_ftr(scr, ftr)
        # draw_projs(scr, projs)
        # draw_enemies(scr, enemies)

        # move_projs(projs)

        # # Collision detection
        # enemies = [e for e in enemies if not e.has_been_popped(projs)]
        # projs = [proj for proj in projs if not proj.collided]

        # pygame.display.flip()


    # pygame.quit()

if __name__ == '__main__':
    main()
