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

bord1 = pg.image.load('images\\border.png')
bord2 = pg.image.load('images\drev.png')
bord3 = pg.image.load('images\gora.png')
bord4 = pg.image.load('images\kust.png')
bord5 = pg.image.load('images\water3.png')
bord6 = pg.image.load('images\water2.png')
bord7 = pg.image.load('images\water.png')
bord8 = pg.image.load('images\water1.png')
bord9 = pg.image.load('images\water4.png')
bord10 = pg.image.load('images\water5.png')
bord11 = pg.image.load('images\water6.png')
bord12 = pg.image.load('images\water7.png')
bord13 = pg.image.load('images\water8.png')
bord14 = pg.image.load('images\\borderB.png')
bord15 = pg.image.load('images\drevB.png')
bord16 = pg.image.load('images\kustB.png')
bord17 = pg.image.load('images\goraB.png')
bord18 = pg.image.load('images\\borderB.png')
bord19 = pg.image.load('images\water6.png')
bord20 = pg.image.load('images\water7.png')
bord21 = pg.image.load('images\water8.png')

bordP = pg.image.load('images\engl.png')
bordL = pg.image.load('images\engl1.png')
bordM = pg.image.load('images\engl3.png')
bordN = pg.image.load('images\engl4.png')
bordF = pg.image.load('images\englB.png')
bordG = pg.image.load('images\engl1B.png')
bordD = pg.image.load('images\engl3B.png')
bordJ = pg.image.load('images\engl4B.png')

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
        self.rect = self.image.get_rect(topleft=(x, y))


def Map_render(maps, surf):
    global rectsB, rectsE, L1stList, L2ndList, P1stList, P2ndList, M1stList, M2ndList, N1stList, N2ndList
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
    y = 0
    for i in maps:
        for j in i:
            if j == '=':
                rectE = pg.Rect(x, y, rectW, rectH)
                rectsE.append(rectE)
                pg.draw.rect(surf, (0, 0, 0), rectE)
            if j == '!':
                rect = pg.Rect(x, y, rectW, rectH)
                rectsB.append(rect)
            if j == '1':
                border = Border(x, y, bord1)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'B':
                border = Border(x, y, bord14)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == '2':
                border = Border(x, y, bord2)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'S':
                border = Border(x, y, bord15)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == '3':
                border = Border(x, y, bord3)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'A':
                border = Border(x, y, bord17)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == '4':
                border = Border(x, y, bord4)
                #border.rect[3] -= 5
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'H':
                border = Border(x, y, bord16)
                #border.rect[3] -= 5
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == '5':
                border = Border(x, y, bord5)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
                 
            if j == '6':
                border = Border(x, y, bord6)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == '7':
                border = Border(x, y, bord7)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == '8':
                border = Border(x, y, bord8)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == '9':
                border = Border(x, y, bord9)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (0, 255, 0), border.rect, 1)
            if j == 'V':
                border = Border(x, y, bord13)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (0, 255, 0), border.rect, 1)
            if j == 'Q':
                border = Border(x, y, bord7)
                rectsB.append(border.rect)
                surf.blit(pg.transform.flip(border.image, True, False), border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'W':
                border = Border(x, y, bord6)
                rectsB.append(border.rect)
                surf.blit(pg.transform.flip(border.image, True, False), border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'Z':
                border = Border(x, y, bord10)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'C':
                border = Border(x, y, bord12)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)
            if j == 'X':
                border = Border(x, y, bord11)
                rectsB.append(border.rect)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.rect(surf, (255, 0, 0), border.rect, 1)

            if j == 'P':
                P1st = (x, y+180)
                P2nd = (x+79, y+79+180)
                P1stList.append(P1st)
                P2ndList.append(P2nd)
                
                subRectp1 = pg.Rect(x, y, 1, 1)
                subRectp2 = pg.Rect(x+79, y+79, 1, 1)
                rectsB.append(subRectp1)
                rectsB.append(subRectp2)

                border = Border(x, y, bordP)
                surf.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectp1.x, subRectp1.y), (subRectp2.x, subRectp2.y))         
            if j == 'L':
                if  i[i.index(j)+1] == 'P':
                    rect = pg.Rect(x, y + 30, rectW*2, 2)
                    rectsB.append(rect)
                    
                L1st = (x+80, y+180)
                L2nd = (x, y+80+180)
                L1stList.append(L1st)
                L2ndList.append(L2nd)

                subRectl1 = pg.Rect(x+80, y, 1, 1)
                subRectl2 = pg.Rect(x, y+79, 1, 1)
                rectsB.append(subRectl1)
                rectsB.append(subRectl2)

                border = Border(x, y, bordL)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectl1.x, subRectl1.y), (subRectl2.x, subRectl2.y))        
            if j == 'M':
                M1st = (x+80, y+180)
                M2nd = (x, y+80+180)
                M1stList.append(M1st)
                M2ndList.append(M2nd)

                subRectm1 = pg.Rect(x+80, y, 1, 1)
                subRectm2 = pg.Rect(x, y+80, 1, 1)
                rectsB.append(subRectm1)
                rectsB.append(subRectm2)

                border = Border(x, y, bordM)
                surf.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectm1.x, subRectm1.y), (subRectm2.x, subRectm2.y))         
            if j == 'N':
                if  i[i.index(j)+1] == 'M':
                    rect = pg.Rect(x, y + 50, rectW*2, 2)
                    rectsB.append(rect)
                N1st = (x, y + 180)
                N2nd = (x+79, y+79+180)
                N1stList.append(N1st)
                N2ndList.append(N2nd)

                subRectn1 = pg.Rect(x, y, 1, 1)
                subRectn2 = pg.Rect(x+79, y+79, 1, 1)
                rectsB.append(subRectn1)
                rectsB.append(subRectn2)

                border = Border(x, y, bordN)
                surf.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectn1.x, subRectn1.y), (subRectn2.x, subRectn2.y))
            if j == 'F':
                P1st = (x, y+180)
                P2nd = (x+79, y+79+180)
                P1stList.append(P1st)
                P2ndList.append(P2nd)
                
                subRectp1 = pg.Rect(x, y, 1, 1)
                subRectp2 = pg.Rect(x+79, y+79, 1, 1)
                rectsB.append(subRectp1)
                rectsB.append(subRectp2)

                border = Border(x, y, bordF)
                surf.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectp1.x, subRectp1.y), (subRectp2.x, subRectp2.y))         
            if j == 'G':
                if  i[i.index(j)+1] == 'F':
                    rect = pg.Rect(x, y + 30, rectW*2, 2)
                    rectsB.append(rect)
                    
                L1st = (x+80, y+180)
                L2nd = (x, y+80+180)
                L1stList.append(L1st)
                L2ndList.append(L2nd)

                subRectl1 = pg.Rect(x+80, y, 1, 1)
                subRectl2 = pg.Rect(x, y+79, 1, 1)
                rectsB.append(subRectl1)
                rectsB.append(subRectl2)

                border = Border(x, y, bordG)
                surf.blit(border.image, border.rect)
                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectl1.x, subRectl1.y), (subRectl2.x, subRectl2.y))        
            if j == 'D':
                M1st = (x+80, y+180)
                M2nd = (x, y+80+180)
                M1stList.append(M1st)
                M2ndList.append(M2nd)

                subRectm1 = pg.Rect(x+80, y, 1, 1)
                subRectm2 = pg.Rect(x, y+80, 1, 1)
                rectsB.append(subRectm1)
                rectsB.append(subRectm2)

                border = Border(x, y, bordD)
                surf.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectm1.x, subRectm1.y), (subRectm2.x, subRectm2.y))         
            if j == 'J':
                if  i[i.index(j)+1] == 'D':
                    rect = pg.Rect(x, y + 50, rectW*2, 2)
                    rectsB.append(rect)
                N1st = (x, y + 180)
                N2nd = (x+79, y+79+180)
                N1stList.append(N1st)
                N2ndList.append(N2nd)

                subRectn1 = pg.Rect(x, y, 1, 1)
                subRectn2 = pg.Rect(x+79, y+79, 1, 1)
                rectsB.append(subRectn1)
                rectsB.append(subRectn2)

                border = Border(x, y, bordJ)
                surf.blit(border.image, border.rect)

                if hbindic == True:
                    pg.draw.line(surf, (255, 0, 0), (subRectn1.x, subRectn1.y), (subRectn2.x, subRectn2.y))
            
            
            
            x += rectW
        y += rectH
        x = 0

rectW = 80
rectH = 80
pW = 80
pH = 80

px = 600
py = 600

zx = 0
zy = 0

dx = 1280
dy = 0

minix = 155
miniy = 155

maps2Darray = maps.maps2Darray
surfArray = maps.surfArray
maps = maps2Darray  

g = 6
h = 10

a = 0
b = 0 

goStat = True

scrollxr = False
scrollxl = False
scrollyu = False
scrollyd = False

hbindic = False

counterx = 0
countery = 0

speed = 10
pspeed = 5

rectsB = []

m = 0

ii = 0
while True:
    ########################################################
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamepad.stop_listening()
            pg.quit()
    ########################################################
    screen.fill((252, 216, 168))
    activSurf = surfArray[g][h]
    activSurf.fill((252, 216, 168))
    subSurf = surfArray[g+a][h+b]
    subSurf.fill((252, 216, 168))

    ########################################################

    pHbRectTOP = pg.Rect(px+15, py+50, 50, 6)
    pHbRectBOTTOM = pg.Rect(px+15, py+80, 50, 6)
    pHbRectRIGHT = pg.Rect(px+65, py+55, 6, 25)
    pHbRectLEFT = pg.Rect(px+10, py+55, 6, 25)
    
    pHbRectLT = pg.Rect(px+10, py+50, 6, 6)
    pHbRectRT = pg.Rect(px+65, py+50, 6, 6)
    pHbRectLB = pg.Rect(px+10, py+80, 6, 6)
    pHbRectRB = pg.Rect(px+65, py+80, 6, 6)

    mainRect = pg.Rect(0, 0, 1280, 180)
    miniMapRect = pg.Rect(10, 10, 320, 160)

    miniMapMRect = pg.Rect(round(minix, 0), round(miniy, 0), 10, 10)

    ########################################################

    keys = pg.key.get_pressed()
    dpad_x = gamepad.buttons.ABS_HAT0X.value
    dpad_y = gamepad.buttons.ABS_HAT0Y.value

    if keys[pg.K_SLASH]:
        hbindic = True
    else:
        hbindic = False

    if px+40 >= width:
        scrollxr = True
        dy = 0
        b = 1
    if px+40 <= -1:
        scrollxl = True
        dy = 0
        b = -1  
    if py+40 <= 180:
        scrollyu = True
        dx = 0
        a = -1
    if py+40 >= height + 1:
        scrollyd = True
        dx = 0
        a = 1

    if scrollxr:
        goStat = False
        dx = width
        if counterx != width:
            px -= speed
            zx -= speed
            minix += 0.1563
            counterx += speed
        else:
            scrollxr = False
            goStat = True
            counterx = 0
            h += b
            zx = 0
            b = 0
    if scrollxl:
        goStat = False
        dx = -1280
        if counterx != 1280:
            px += speed
            zx += speed
            minix -= 0.1563
            counterx += speed
        else:
            scrollxl = False
            goStat = True
            counterx = 0
            #minix -= 20
            h += b
            zx = 0
            b = 0
    if scrollyu:
        goStat = False
        dy = -height + 180
        if countery != 800:
            py += speed
            zy += speed
            miniy -= 0.25
            countery += speed
        else:
            scrollyu = False
            goStat = True
            countery = 0
            #miniy -= 20
            g += a
            zy = 0
            a = 0
    if scrollyd:
        goStat = False
        dy = height - 180
        if countery != 800:
            py -= speed
            zy -= speed
            miniy += 0.25
            countery += speed
        else:
            scrollyd = False
            goStat = True
            countery = 0
            #miniy += 20
            g += a
            zy = 0
            a = 0

    Map_render(maps[g+a][h+b], surfArray[g+a][h+b])
    Map_render(maps[g][h], surfArray[g][h])
    for i in rectsB:
        i[1] += 180

    if goStat:
        if (keys[pg.K_w] or dpad_y == -1):
            if ii % 22 == 0:
                m = 1
                pActiveAnimF = pAnimF1b
            elif ii % 22 == 11:
                m = 2
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
                m = 3
                pActiveAnimF = pAnimF2f
            elif ii % 22 == 11:
                m = 4
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
                m = 5
                pActiveAnimF = pAnimF2l
            elif ii % 22 == 11:
                m = 6
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
                m = 7
                pActiveAnimF = pAnimF2r
            elif ii % 22 == 11:
                m = 8
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
    
    screen.blit(surfArray[g][h], (zx, zy+180))
    screen.blit(surfArray[g+a][h+b], (zx + dx, zy + dy+180))

    #if hbindic:
    #    for i in rectsB:
    #        pg.draw.rect(screen, (255, 255, 255), i, 1)

    screen.blit(p.image, p.rect)

    #pg.draw.rect(screen, (255, 0, 0), p.rect, 1)

    #pg.draw.rect(screen, (255, 0, 0), pHbRectTOP)
    #pg.draw.rect(screen, (255, 0, 0), pHbRectBOTTOM)
    #pg.draw.rect(screen, (255, 0, 0), pHbRectRIGHT)
    #pg.draw.rect(screen, (255, 0, 0), pHbRectLEFT)

    #pg.draw.rect(screen, (0, 255, 0), pHbRectLT)
    #pg.draw.rect(screen, (0, 255, 0), pHbRectRT)
    #pg.draw.rect(screen, (0, 255, 0), pHbRectLB)
    #pg.draw.rect(screen, (0, 255, 0), pHbRectRB)

    pg.draw.rect(screen, (0, 0, 0), mainRect)
    pg.draw.rect(screen, (128, 128, 128), miniMapRect)
    pg.draw.rect(screen, (0, 255, 0), miniMapMRect)

    ii += 1
    if ii == 91:
        ii = 0

    ########################################################
    pg.display.update()
    clock.tick(FPS)