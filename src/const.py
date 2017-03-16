__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

"""The game's constants.

    Data:
        NAME (str): The game's name.
        AUTHOR (str): The game's author.
        VERSION (str): The game's version.

        SCREEN_RES ((int,int)): The screen resolution.

        TITLE_FONT_SIZE (int): The size of the game's title font.
        FONT_SIZE (int): The size of the game's general font.

        FIGHTER_COLORS ([str]): Available fighter colors.
        ENEMY_COLORS ([str]): Available enemy colors.

        RES_DIR (str): The game's resource directory.
        FONT_RES_DIR (str): The game's font resource directory.
        IMG_RES_DIR (str): The game's image resource directory.
        AUDIO_RES_DIR (str): The game's audio resource directory.

        TITLE_FONT_FILE (str): The game's
        FONT_FILE (str):

        BG_IMG_FILE (str):
        FIGHTER_IMG_FILE_FMT (str):
        PROJECTILE_IMG_FILE_FMT (str):
        ENEMY_IMG_FILE_FMT (str):

        MAIN_MENU_ITEMS (str):
        GAME_MODES (str):

        FIGHTER_SPEED (int):
        FIGHTER_PROJECTILE_SPEED (int):
        ENEMY_SPEED_RNG ((int,int)):
        ENEMY_PROJECTILE_SPEED_RNG ((int,int)):

        FRAMERATE (int):

"""

import os

game_name = 'Fighter'
game_author = 'Dominic Gomez'
VERSION = None

SCREEN_RES = (600,800)

TITLE_FONT_SIZE = 12
FONT_SIZE = 12

FIGHTER_COLORS = ['blue','green','orange','red']
ENEMY_COLORS = ['black','blue','green','red']

RES_DIR = os.path.join('..', 'res')
FONT_RES_DIR = os.path.join(__RES_DIR, 'font')
IMG_RES_DIR = os.path.join(__RES_DIR, 'img')
AUDIO_RES_DIR = os.path.join(__RES_DIR, 'audio')

TITLE_FONT_FILE = os.path.join(__FONT_RES_DIR, 'title_font.ttf')
FONT_FILE = os.path.join(__FONT_RES_DIR, 'font.ttf')

BG_IMG_FILE = os.path.join(__IMG_RES_DIR, 'bg_blue_stars.png')
FIGHTER_IMG_FILE_FMT = os.path.join(__IMG_RES_DIR, 'fighter_{color}.png')
PROJECTILE_IMG_FILE_FMT = os.path.join(__IMG_RES_DIR, 'proj.png')
ENEMY_IMG_FILE_FMT = os.path.join(__IMG_RES_DIR, 'enemy_{color}.png')

MAIN_MENU_ITEMS = ['play','high scores','settings']
GAME_MODES = ['standard','survival']

FIGHTER_SPEED = 5
FIGHTER_PROJECTILE_SPEED = 10
ENEMY_SPEED_RNG = (0,10)
ENEMY_PROJECTILE_SPEED_RNG = ()

FRAMERATE = 60
