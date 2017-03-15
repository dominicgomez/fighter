__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

"""The game's constants."""

import os

# A path to the game's resources directory:
RES_DIR = os.path.join('..', 'res')

# Paths to image files:
BG_IMG = os.path.join(RES_DIR, 'bg.png')
FTR_IMG = os.path.join(RES_DIR, 'ftr.png')
PROJ_IMG = os.path.join(RES_DIR, 'proj.png')
ENEMY_IMG = os.path.join(RES_DIR, 'enemy.png')

# Screen size:
SCR_W = 800
SCR_H = 1000

# The number of pixels that the fighter moves for each key press.
FTR_X_DELTA = 5
FTR_Y_DELTA = 5

# The number of pixels that projectiles move each frame.
PROJ_DELTA = 10

# I don't really know how this works
FRAMERATE = 60
