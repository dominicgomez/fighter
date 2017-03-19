__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

"""Configuration and settings.

Data:
    screen_res ((int,int)): The screen resolution.
    framerate (int):

    res_dir (str): The game's resource directory.
    font_res_dir (str): The game's font resource subdirectory.
    img_res_dir (str): The game's image resource subdirectory.
    audio_res_dir (str): The game's audio resource subdirectory.

    title_font_size (int): The size of the game's title font.
    font_size (int): The size of the game's general font.
    title_font_file (str): The game's title font file.
    font_file (str): The game's general font file.

    bg_img_file (str): The game's background image file.

    fighter_colors ([str]): Available fighter colors. Should match the names of
        the appropriate files in the image resource subdirectory.
    fighter_img_file_fmt (str): The game's fighter image file format. The
        placeholder should be replaced with a value from fighter_colors to
        obtain a path to a fighter image file.
    fighter_speed (int): The fighter's speed in pixels per frame.
    fighter_projectile_speed (int): The fighter's projectile's speed in pixels
        per frame.

    enemy_colors ([str]): Available enemy colors. Should match the names of the
        appropriate files in the image resource subdirectory.
    enemy_img_file_fmt (str): The game's enemy image file format. The
        placeholder should be replaced with a value from enemy_colors to obtain
        a path to a enemy image file.
    enemy_speed_rng ((int,int)): The (inclusive) upper and lower limits of the
        enemies' speeds.
    enemy_projectile_speed_rng ((int,int)): The (inclusive) upper and lower
        limits of the enemies' projectiles' speeds.

    projectile_types ([str]): Available projectile types. Should match the
        names of the appropriate files in the image resource subdirectory.
    projectile_img_file_fmt (str): The game's projectile image file format.
        The placeholder should be replaced with a value from projectile_types
        to obtain a path to a projectile image file.

"""

# Display
# -------
screen_res = (600,800)
framerate = 60

# Resource Directories
# --------------------
res_dir = os.path.join('..', 'res')
font_res_dir = os.path.join(res_dir, 'font')
img_res_dir = os.path.join(res_dir, 'img')
audio_res_dir = os.path.join(res_dir, 'audio')

# Font
# ----
title_font_size = 12
font_size = 12
title_font_file = os.path.join(font_res_dir, 'title_font.ttf')
font_file = os.path.join(font_res_dir, 'font.ttf')

# Background
# ----------
bg_img_file = os.path.join(img_res_dir, 'bg_blue_stars.png')

# Enemy
# -----
enemy_colors = ['black','blue','green','red']
enemy_img_file_fmt = os.path.join(img_res_dir, 'enemy_{color}.png')
enemy_speed_rng = (0,10)
enemy_projectile_speed_rng = (5,15)

# Projectile
# ----------
projectile_types = ['fighter','enemy']
projectile_img_file_fmt = os.path.join(img_res_dir, 'proj_{type}.png')
