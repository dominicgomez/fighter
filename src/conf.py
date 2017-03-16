__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

"""Configuration and settings.

    Data:
        game_name (str): The game's name.
        game_author (str): The game's author.
        game_version (str): The game's version.

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

game_name = 'Fighter'
game_author = 'Dominic Gomez'
game_version = None

screen_resolution = (600,800)

framerate = 60

title_font_size = 12
font_size = 12

fighter_colors = ['blue','green','orange','red']
enemy_colors = ['black','blue','green','red']

res_dir = os.path.join('..', 'res')
font_res_dir = os.path.join(res_dir, 'font')
img_res_dir = os.path.join(res_dir, 'img')
audio_res_dir = os.path.join(res_dir, 'audio')

title_font_file = os.path.join(font_res_dir, 'title_font.ttf')
font_file = os.path.join(font_res_dir, 'font.ttf')

bg_img_file = os.path.join(img_res_dir, 'bg_blue_stars.png')
fighter_img_file_fmt = os.path.join(img_res_dir, 'fighter_{color}.png')
projectile_img_file_fmt = os.path.join(img_res_dir, 'proj.png')
enemy_img_file_fmt = os.path.join(img_res_dir, 'enemy_{color}.png')

main_menu_items = ['play','high scores','settings']
game_modes = ['standard','survival']

fighter_speed = 5
fighter_projectile_speed = 10
enemy_speed_rng = (0,10)
enemy_projectile_speed_rng = (5,15)
