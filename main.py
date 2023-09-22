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
#gamepad.listen()

surf = pg.Surface((width, 180))

rectW = 80
rectH = 80

px = 600
py = 600

pW = 64
pH = 64

minix = 155
miniy = 155

pspeed = 5

mapsxLim = [-2, 1282]
mapsyLim = [178, 982]

maps2Darray = maps.maps2Darray
Dmaps2Darray = maps.Dmaps2Darray

g = 7
h = 8
g1 = 2
h1 = 0
minig = 2
minig = 1

activeInd = [g, h]

maps = maps2Darray[g][h]

bord1 = pg.image.load('images\\border.png')
bord2 = pg.image.load('images\drev.png')
bord3 = pg.image.load('images\gora.png')
bord4 = pg.image.load('images\kust.png')
bord5 = pg.image.load('images\water3.png')
bord6 = pg.image.load('images\water2.png')
bord7 = pg.image.load('images\water.png')
bord8 = pg.image.load('images\water1.png')
bord9 = pg.image.load('images\water4.png')
bordP = pg.image.load('images\engl.png')
bordL = pg.image.load('images\engl1.png')
bordM = pg.image.load('images\engl3.png')
bordN = pg.image.load('images\engl4.png')

pAnimF1f = pg.image.load('images\player1f.png')
pAnimF2f = pg.image.load('images\player2f.png')
pAnimF1r = pg.image.load('images\player1r.png')
pAnimF2r = pg.image.load('images\player2r.png')
pAnimF1l = pg.image.load('images\player1l.png')
pAnimF2l = pg.image.load('images\player2l.png')
pAnimF1b = pg.image.load('images\player1b.png')
pAnimF2b = pg.image.load('images\player2b.png')

pActiveAnimF = pAnimF1f

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

demention = 0

col = (0, 255, 0)
lineIsColLT = False
lineIsColRT = False
lineIsColLB = False
lineIsColRB = False

hbindic = False

ii = 0
while True:
    ########################################################
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamepad.stop_listening()
            pg.quit()
    ########################################################
    screen.fill((252, 216, 168))

    pRect = pg.Rect(px-32, py-32, pW, pH)

    pHbRectTOP = pg.Rect(px-32, py+4, pW-5, 4)
    pHbRectBOTTOM = pg.Rect(px-32, py+36, pW-5, 5)
    pHbRectRIGHT = pg.Rect(px+27, py+8, 4, pH - 36)
    pHbRectLEFT = pg.Rect(px-36, py+8, 4, pH - 36)

    pHbRectLT = pg.Rect(px-36, py+4, 7, 7)
    pHbRectRT = pg.Rect(px+25, py+4, 7, 7)
    pHbRectLB = pg.Rect(px-36, py+35, 7, 7)
    pHbRectRB = pg.Rect(px+25, py+35, 7, 7)

    mainRect = pg.Rect(0, 0, 1280, 180)
    miniMapRect = pg.Rect(10, 10, 320, 160)

    miniMapMRect = pg.Rect(minix, miniy, 10, 10)
    #####################Map Randering######################
    ########################################################
    rectsB = []
    rectsE = []
    L1stList = []
    L2ndList = []
    P1stList = []
    P2ndList = []
    M1stList = []
    M2ndList = []
    N1stList = []
    N2ndList = []

    x = 0
    y = 180
    for i in maps:
        for j in i:
            if j == '=':
                rectE = pg.Rect(x, y, rectW, rectH)
                rectsE.append(rectE)
                pg.draw.rect(screen, (0, 0, 0), rectE)
            if j == '!':
                rect = pg.Rect(x, y, rectW, rectH)
                rectsB.append(rect)
            if j == '1':
                border = Border(x, y, bord1)
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
            if j == '2':
                border = Border(x, y, bord2)
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
            if j == '3':
                border = Border(x, y, bord3)
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
            if j == '4':
                border = Border(x, y, bord4)
                border.rect[3] -= 5
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)     
            if j == '5':
                border = Border(x, y, bord5)
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
                 
            if j == '6':
                border = Border(x, y, bord6)
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
            if j == '7':
                border = Border(x, y, bord7)
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
            if j == '8':
                border = Border(x, y, bord8)
                rectsB.append(border.rect)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
            if j == '9':
                border = Border(x, y, bord9)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (0, 255, 0), border.rect, 1)
            if j == 'Q':
                border = Border(x, y, bord7)
                rectsB.append(border.rect)
                screen.blit(pg.transform.flip(border.image, True, False), border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)
            if j == 'W':
                border = Border(x, y, bord6)
                rectsB.append(border.rect)
                screen.blit(pg.transform.flip(border.image, True, False), border.rect)
                if hbindic == True:
                    pg.draw.rect(screen, (255, 0, 0), border.rect, 1)

            if j == 'P':
                P1st = (x, y)
                P2nd = (x+79, y+79)
                P1stList.append(P1st)
                P2ndList.append(P2nd)
                
                subRectp1 = pg.Rect(x, y, 1, 1)
                subRectp2 = pg.Rect(x+79, y+79, 1, 1)
                rectsB.append(subRectp1)
                rectsB.append(subRectp2)

                border = Border(x, y, bordP)
                screen.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(screen, (255, 0, 0), P1st,  P2nd)         
            if j == 'L':
                L1st = (x+80, y)
                L2nd = (x, y+80)
                L1stList.append(L1st)
                L2ndList.append(L2nd)

                subRectl1 = pg.Rect(x+80, y, 1, 1)
                subRectl2 = pg.Rect(x, y+80, 1, 1)
                rectsB.append(subRectl1)
                rectsB.append(subRectl2)

                border = Border(x, y, bordL)
                screen.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.line(screen, (255, 0, 0), L1st, L2nd)        
            if j == 'M':
                M1st = (x+80, y)
                M2nd = (x, y+80)
                M1stList.append(M1st)
                M2ndList.append(M2nd)

                subRectm1 = pg.Rect(x+80, y, 1, 1)
                subRectm2 = pg.Rect(x, y+80, 1, 1)
                rectsB.append(subRectm1)
                rectsB.append(subRectm2)

                border = Border(x, y, bordM)
                screen.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(screen, (255, 0, 0), M1st,  M2nd)         
            if j == 'N':
                N1st = (x, y)
                N2nd = (x+79, y+79)
                N1stList.append(N1st)
                N2ndList.append(N2nd)

                subRectn1 = pg.Rect(x, y, 1, 1)
                subRectn2 = pg.Rect(x+79, y+79, 1, 1)
                rectsB.append(subRectn1)
                rectsB.append(subRectn2)

                border = Border(x, y, bordN)
                screen.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(screen, (255, 0, 0), N1st,  N2nd)
            x += rectW
        y += rectH
        x = 0
    ########################################################

    ##############Rectangular Coordinates###################

    if hbindic == True:
        pg.draw.rect(screen, (255, 0, 0), pHbRectTOP)
        pg.draw.rect(screen, (255, 0, 0), pHbRectBOTTOM)
        pg.draw.rect(screen, (255, 0, 0), pHbRectLEFT)
        pg.draw.rect(screen, (255, 0, 0), pHbRectRIGHT)

        pg.draw.rect(screen, col, pHbRectLT)
        pg.draw.rect(screen, col, pHbRectLB)
        pg.draw.rect(screen, col, pHbRectRB)
        pg.draw.rect(screen, col, pHbRectRT)
    ########################################################
    keys = pg.key.get_pressed()

    if keys[pg.K_SLASH]:
        hbindic = True
    else: 
        hbindic = False

    ########################Movement########################
    
    dpad_x = gamepad.buttons.ABS_HAT0X.value
    dpad_y = gamepad.buttons.ABS_HAT0Y.value

    if (keys[pg.K_w] or dpad_y == -1):
        pActiveAnimF = pAnimF1b
        if ii % 22 == 0:
            pActiveAnimF = pAnimF1b
        else:
            pActiveAnimF = pAnimF2b
        
        if pHbRectTOP.collidelist(rectsB) == -1:
            for i in range(len(P1stList)):
                if pHbRectRT.clipline(P1stList[i], P2ndList[i]):
                    px -= pspeed
            for i in range(len(L1stList)):
                if pHbRectLT.clipline(L1stList[i], L2ndList[i]):
                    px += pspeed
            py -= pspeed    
    
    elif (keys[pg.K_s] or dpad_y == 1):

        if ii % 22 == 0:
            pActiveAnimF = pAnimF2f
        elif ii % 22 == 11:
            pActiveAnimF = pAnimF1f

        if pHbRectBOTTOM.collidelist(rectsB) == -1:
            for i in range(len(M1stList)):
                if pHbRectRB.clipline(M1stList[i], M2ndList[i]):
                    px -= pspeed
            for i in range(len(N1stList)):
                if pHbRectLB.clipline(N1stList[i], N2ndList[i]):
                    px += pspeed
            py += pspeed

    elif (keys[pg.K_a] or dpad_x == -1):

        if ii % 22 == 0:
            pActiveAnimF = pAnimF2l
        elif ii % 22 == 11:
            pActiveAnimF = pAnimF1l

        if pHbRectLEFT.collidelist(rectsB) == -1:
            for i in range(len(L1stList)):
                if pHbRectLT.clipline(L1stList[i], L2ndList[i]):
                    py += pspeed
            for i in range(len(N1stList)):
                if pHbRectLB.clipline(N1stList[i], N2ndList[i]):
                    py -= pspeed
            px -= pspeed

    elif (keys[pg.K_d] or dpad_x == 1):

        if ii % 22 == 0:
                pActiveAnimF = pAnimF2r
        elif ii % 22 == 11:
            pActiveAnimF = pAnimF1r

        if pHbRectRIGHT.collidelist(rectsB) == -1:
            for i in range(len(P1stList)):
                if pHbRectRT.clipline(P1stList[i], P2ndList[i]):
                    py += pspeed
            for i in range(len(M1stList)):
                if pHbRectRB.clipline(M1stList[i], M2ndList[i]):
                    py -= pspeed
            px += pspeed

    p = Player(px, py, pActiveAnimF)
    screen.blit(p.image, p.rect)

    
    if ii == 90:
        ii = 0
    ii += 1

    #p = pg.draw.rect(screen, (0, 255, 0), pRect)
    ########################################################

    pg.draw.rect(screen, (0, 0, 0), mainRect)
    pg.draw.rect(screen, (128, 128, 128), miniMapRect)
    pg.draw.rect(screen, (0, 255, 0), miniMapMRect)
    
    ######################Map Swither#######################
    if demention == 0 and pHbRectBOTTOM.collidelist(rectsE) != -1:
        px = 640
        py = 852
        activeInd = [g1, h1]
        demention = 1
    elif demention == 1 and pHbRectTOP.collidelist(rectsE) != -1:
        px = 360
        py = 228
        activeInd = [g, h]
        demention = 0

    if py <= mapsyLim[0]:
        activeInd[0] -= 1
        py = mapsyLim[1] - 4 #978
        miniy -= 20
    elif py >= mapsyLim[1]:
        activeInd[0] += 1
        py = mapsyLim[0] + 4 #182
        miniy += 20
    elif px <= mapsxLim[0]:
        activeInd[1] -= 1
        px = mapsxLim[1] - 4 #1278
        minix -= 20
    elif px >= mapsxLim[1]:
        activeInd[1] += 1
        px = mapsxLim[0] + 4 #2
        minix += 20

    if demention == 0:
        maps = maps2Darray[activeInd[0]][activeInd[1]]
    elif demention == 1:
        maps = Dmaps2Darray[activeInd[0]][activeInd[1]]
    ########################################################
    #print(f'X: {px, g}  Y: {py, h}\n')
    #print(dpad_x, dpad_y)
    #print('\r', end = '')
    #print(miniMapMatrix, miniMapMatrix[activeInd[0]][activeInd[1]])
    ########################################################

    pg.display.update()
    clock.tick(FPS)
