__author__ = 'Dominic Gomez'
__email__ = 'DominicAnthonyGomez@gmail.com'

import abc
import pygame

class Scene(abc.ABC):
    """This is the abstract base class for a game scene: It cannot be
    instantiated, and all classes that inherit from it must implement its
    methods.

    """

    def __init__(self):
        super(Scene, self).__init__()

    @abc.abstractmethod
    def draw(self, game):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def handle_event(self, event, keys):
        pass

class TitleScene(Scene):
    # TODO: Maybe make all of the screen's components a tuple (a,b), where a is
    # the thing to display (like the rasterized label) and b is the ordered
    # pair pointing to its upper left hand corner. These could also be the
    # values for a map whose keys are the names of the scenes:
    # 'title','play','high scores','settings'.
    # I could also just have a separate list with all of the scenes, but I
    # think I like the map idea more.
    # Just some thoughts. I'm really sleepy. I didn't sleep last night, and all
    # I've had is really strong coffee. That's crazy. I should really get some
    # sleep.
    """The game's first screen."""

    def __init__(self, screen):
        # The options to choose from on the title screen, mapped to their positions
        # on the title screen.
        self.options = {
            'play' : None,
            'high scores' : None,
            'settings' : None
        }

    def draw(self, screen, title_font_file, title_font_size, font_file,
            font_size, name):
        selector_pos = self.__draw_title(screen, title_font_file,
                title_font_size, name)
        self.draw_options(screen, selector_pos, font_file, font_size)

    def update(self):
        pass

    def handle_event(self, event, keys):
        pass

    def __draw_title(self, screen, title_font_file, title_font_size, name):
        title_font = pygame.font.Font(title_font_file, title_font_size)
        title_label = title_font.render(name, True, (0,0,0))
        title_pos = self.__get_title_pos(screen.get_rect(),
                                        title_label.get_rect())
        screen.blit(title_label, title_pos)
        return title_label.get_rect(topleft=title_pos).bottomleft

    def __get_title_pos(self, screen_rect, title_rect):
        # Get the center of the screen, and offset the title appropriately.
        x = screen_rect.centerx - int(title_rect.width / 2)
        y = screen_rect.centery - int(title_rect.height / 2)
        return (x,y)

    def draw_options(self, screen, selector_pos, font_file, font_size):
        font = pygame.font.Font(font_file, font_size)
        selector = font.render('*', True, (0,0,0))
        # screen.blit(selector, selector_pos)
        option_pos = (selector_pos[0]+selector.get_width(),selector_pos[1])
        for option in self.options:
            self.options[option] = option_pos
            option_label = font.render(option, True, (0,0,0))
            screen.blit(option_label, option_pos)
            option_pos = (option_pos[0],option_pos[1]+option_label.get_height())
        screen.blit(selector, (self.options['settings'][0]-selector.get_width(),
                               self.options['settings'][1]))
