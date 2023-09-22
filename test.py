from pygamepad.gamepads.default import Gamepad
import pygame as pg
import maps as maps

width = 1280
height = 980

FPS = 90
pg.init()

gamepad = Gamepad()

screen = pg.display.set_mode((width, height))
pg.display.set_caption('game.')
clock = pg.time.Clock()

surf0 = pg.Surface((1280, 800))
surf1 = pg.Surface((1280, 800))

surf3 = pg.Surface((1280, 800))
surf4 = pg.Surface((1280, 800))
surf5 = pg.Surface((1280, 800))

surfArray = [surf0, surf1]

rectW = 80
rectH = 80

px = 600
py = 600

pAnimF1f = pg.image.load('images\player1f.png')

bord1 = pg.image.load('images\\border.png')
bord2 = pg.image.load('images\drev.png')


class Border(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

maps2Darray = maps.maps2Darray

g = 7
h = 7

activeInd = [g, h]

maps = maps2Darray

def Map_render(maps, activeSurf, activeInd):
    x = 0
    y = 0
    for i in maps[activeInd[0]][activeInd[1]]:
        for j in i:
            if j == '=':
               rectE = pg.Rect(x, y, rectW, rectH)
               pg.draw.rect(activeSurf, (0, 0, 0), rectE)
            if j == '1':
                border = Border(x, y, bord1)
                activeSurf.blit(border.image, border.rect)

            if j == '2':
                border = Border(x, y, bord2)
                activeSurf.blit(border.image, border.rect)
            x += rectW
        y += rectH
        x = 0
    

goStat = True

zx = 0
zy = 0

szx = 1280
szy = 0

indx = 0
indy = 0

mainSurf = surfArray[0]
subSurf = surfArray[1]

ScrollCounterx = 0
ScrollCountery = 0

scrollStatXR = False
scrollStatXL = False
scrollStatYB = False
scrollStatYU = False

surfSwapStat = False
a = 0 
while True:
    ########################################################
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamepad.stop_listening()
            pg.quit()
    ########################################################
    screen.fill((252, 216, 168))
    mainSurf.fill((252, 216, 168))
    subSurf.fill((252, 216, 168))


    Map_render(maps, mainSurf, activeInd)
    
    if px >= 1275:
        scrollStatXR = True
        indx = 1
    if px <= 0:
        scrollStatXL = True
        indx = -1

    if py >= 975:
        scrollStatYB = True
    if py <= 180:
        scrollStatYU = True
    
    if scrollStatXR:
        goStat = False
        
        if ScrollCounterx != 1280:
            zx -= 10
            szx -= 10
            px -= 10
            ScrollCounterx += 10
            if px - 40 <= 0:
                px = 40
        else:
            scrollStatXR = False
            goStat = True
            surfSwapStat = True
            ScrollCounterx = 0

    if surfSwapStat:
        a = mainSurf
        mainSurf = subSurf
        subSurf = a
        surfSwapStat = False
    
    Map_render(maps, subSurf, [activeInd[0], activeInd[1]+indx])



    

    

    #if ScrollCounterx == 1280:
    #    ScrollCounterx = 0

    
    
            


    keys = pg.key.get_pressed()

    if goStat:
        if keys[pg.K_w]:
            py -= 5
            #zy += 1
        elif keys[pg.K_s]:
            py += 5
            #zy -= 1
        elif keys[pg.K_a]:
            px -= 5
            #zx += 1
        elif keys[pg.K_d]:
            px += 5
            #zx -= 1

    screen.blit(mainSurf, (zx, zy+180))
    screen.blit(subSurf, (szx, szy+180))

    p = Player(px, py, pAnimF1f)
    screen.blit(p.image, p.rect)

    mainRect = pg.Rect(0, 0, 1280, 180)
    pg.draw.rect(screen, (0, 0, 0), mainRect)

    print(mainSurf, subSurf)

    ########################################################
    pg.display.update()
    clock.tick(FPS)
