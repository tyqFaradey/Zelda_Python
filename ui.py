import pygame as pg
from settings import *

class Interface:
    def __init__(self):
        self.surf = pg.Surface((width, 180))
        self.minimap_surf = pg.Surface((320, 160))

        self.lifes = font30.render('-LIFE-', 0, (208, 44, 0))
        self.xleb = font30.render('x', 0, (255, 255, 255))
        self.num = font30.render(f'{0}', 0, (255, 255, 255))

    def minimap(self, ind):
        self.minimap_surf.fill((127,127,127))
        mini_rect = pg.Rect((ind[0]*20 + 5, ind[1]*20 + 5), (10,10))
        pg.draw.rect(self.minimap_surf, (0,255,0), mini_rect)

    def hearts(self):
        pass


    def rendering(self, ind):
        self.surf.fill((0,0,0))
        self.minimap(ind)

        self.surf.blit(self.minimap_surf, (10,10))
        self.surf.blit(images[100], (340, 20))
        self.surf.blit(self.xleb, (373, 20))
        self.surf.blit(self.num, (400, 20))

        self.surf.blit(images[1002], (500, 15))
        self.surf.blit(images[1001], (630, 15))

        self.surf.blit(self.lifes, (780, 50))

        rect = ()

        #pg.draw.rect(self.surf, (255,255,255), (490,20,100,140))
        #pg.draw.rect(self.surf, (255,255,255), (620,20,100,140))
        










