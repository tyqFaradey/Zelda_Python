import pygame as pg
from settings import *

class Menu:
    def __init__(self, font) -> None:

        self.menu_surf = pg.Surface((width, height))

        self.game_stat = 0

        self.font = pg.font.Font('the-legend-of-zelda-nes.ttf', 50)
        self.font100 = pg.font.Font('the-legend-of-zelda-nes.ttf', 100)

        self.texts = ['play', 'help', 'quit']

        self.option_buttons = [
            self.font.render(self.texts[0], 0, (231, 90, 16)),
              self.font.render(self.texts[1], 0, (231, 90, 16)),
                self.font.render(self.texts[2], 0, (231, 90, 16))]
        
        self.callbacks = [1, 'help', 499]
        self.current_button_index = 0

    def switch(self, direction):
        #self.current_button_index = max(0, min(self.current_button_index + direction, len(self.option_buttons)-1))
        self.current_button_index = self.current_button_index + direction
        if self.current_button_index > len(self.option_buttons)-1:
            self.current_button_index = 0
        if self.current_button_index < 0:
            self.current_button_index = len(self.option_buttons)-1

    def select(self):
        return self.callbacks[self.current_button_index]

    def rendering(self, x, y, surf):
        surf.fill((247, 200, 193))
        logo_rect = images[1000].get_rect()
        logo_rect.midtop = (surf.get_size()[0]//2, 100)

        surf.blit(images[1000], logo_rect)


        for ind, button in enumerate(self.option_buttons):
            button_rect = button.get_rect()
            button_rect.midtop = (x, y + ((button_rect.height + 20)*ind))
            button_rect.width += 3
            if ind == self.current_button_index:
                button = self.font.render(self.texts[ind], 0, (255, 165, 66))
                #pg.draw.rect(surf, (255,255,255), ((button_rect.x-3, button_rect.y-3), (button_rect.width, button_rect.height+3)))

            surf.blit(button, button_rect)

    def help(self, surf):
        surf.fill((0,0,0))
        help_text = 'HELP.'
        text = self.font100.render(help_text, 0, (255,255,255))
        rect = text.get_rect()
        
        rect.center = (surf.get_size()[0] // 2 + 50, surf.get_size()[1] // 2)
        
        surf.blit(text, rect)
