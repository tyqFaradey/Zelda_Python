from pygamepad.gamepads.default import Gamepad
import pygame as pg
import os
from os import walk
from debug import debug
from settings import *
from menu import Menu
from player import Player
from ui import Interface
from enemy import Enemy


os.environ['SDL_VIDEO_WINDOW_POS'] = "850, 40"

pg.init()
gamepad = Gamepad()

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Zelda')
clock = pg.time.Clock()

menu_surf = pg.Surface((width, height))

bg_surf = pg.Surface((width, height-180))

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, image, stat):
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        match stat:
            case 1:
                self.hitbox = pg.Rect(self.rect.topleft, (self.rect.width, self.rect.height - tile_size//2))
                self.hitbox1 = pg.Rect((self.rect.x + tile_size//2, self.rect.y), (self.rect.width - tile_size//2, self.rect.height))    
            case 2:
                self.hitbox = pg.Rect(self.rect.topleft, (self.rect.width, self.rect.height - tile_size//2))
                self.hitbox1 = pg.Rect(self.rect.topleft, (self.rect.width - tile_size//2, self.rect.height))
            case 3:
                self.hitbox = pg.Rect((self.rect.x, self.rect.y + tile_size//2), (self.rect.width, self.rect.height - tile_size//2))
                self.hitbox1 = pg.Rect((self.rect.x + tile_size//2, self.rect.y), (self.rect.width - tile_size//2, self.rect.height))
            case 4:
                self.hitbox = pg.Rect((self.rect.x, self.rect.y + tile_size//2), (self.rect.width, self.rect.height - tile_size//2))
                self.hitbox1 = pg.Rect(self.rect.topleft, (self.rect.width - tile_size//2, self.rect.height))
            case _:
                self.hitbox = self.rect.inflate(0, 0)
                

def map_rendering(world, ind, zx, zy):
    global obstacle_sprites, enter_sprites
    obstacle_sprites = []
    enter_sprites = []
    for row_ind, row in enumerate(world[ind[1]][ind[0]]):
            for col_ind, col in enumerate(row):
                x = zx + col_ind * tile_size
                y = zy + row_ind * tile_size + 180
                match col:
                    case '=':
                        tile = Tile((x,y), images[0], 0)
                        enter_sprites.append(tile.rect)
                        pg.draw.rect(screen, (0, 0, 0), tile.rect)
                    case '0':
                        tile = Tile((x,y), images[0], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '1':
                        tile = Tile((x,y), images[1], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '2':
                        tile = Tile((x,y), images[2], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '3':
                        tile = Tile((x,y), images[3], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '4':
                        tile = Tile((x,y), images[4], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '5':
                        tile = Tile((x,y), images[5], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '6':
                        tile = Tile((x,y), images[6], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '7':
                        tile = Tile((x,y), images[7], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case '8':
                        tile = Tile((x,y), images[8], 0)
                        screen.blit(tile.image, tile.rect)     
                    case '9':
                        tile = Tile((x,y), images[12], 0)
                        screen.blit(tile.image, tile.rect)
                    case 'a':
                        tile = Tile((x,y), images[13], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case 's':
                        tile = Tile((x,y), images[16], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case 'd':
                        tile = Tile((x,y), images[14], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case 's':
                        tile = Tile((x,y), images[15], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case 'z':
                        tile = Tile((x,y), images[11], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case 'x':
                        tile = Tile((x,y), images[9], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    case 'c':
                        tile = Tile((x,y), pg.transform.flip(images[5], True, False), 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)

                    case 'q':
                        tile = Tile((x,y), images[21], 1)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)
                    case 'w':
                        tile = Tile((x,y), images[22], 2)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)
                    case 'e':
                        tile = Tile((x,y), images[23], 3)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)
                    case 'r':
                        tile = Tile((x,y), images[24], 4)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)

                    case 't':
                        tile = Tile((x,y), images[25], 1)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)
                    case 'y':
                        tile = Tile((x,y), images[26], 2)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)
                    case 'u':
                        tile = Tile((x,y), images[27], 3)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)
                    case 'i':
                        tile = Tile((x,y), images[28], 4)
                        obstacle_sprites.append(tile.hitbox)
                        obstacle_sprites.append(tile.hitbox1)
                        screen.blit(tile.image, tile.rect)

                    case '/':
                        tile = Tile((x,y), images[14], 0)
                        obstacle_sprites.append(tile.hitbox)
                        screen.blit(tile.image, tile.rect)
                    #case 'O':
                    #    enemy = Enemy('octorok', (x,y))
                    #    screen.blit(enemy.image, enemy.rect)


def map_scrolling():
    global a, sotw_direction, demention, go_stat, zx, zy, dx, dy, ind, scroll_direction, scroll, scroll_speed, map_mrect
    
    if player.hitbox.centery <= 180-1 and player.hitbox.centery >= 170:
        sotw_direction['N'] = True
        scroll_direction[1] = -1

    elif player.hitbox.centery >= height+1 and player.hitbox.centery <= height+10:
        sotw_direction['S'] = True
        scroll_direction[1] = 1

    elif player.rect.centerx <= 0-1:
        sotw_direction['W'] = True
        scroll_direction[0] = -1

    elif player.rect.centerx >= width+1:
        sotw_direction['E'] = True
        scroll_direction[0] = 1

    if player.enter_stat:
        go_stat = False
        if demention == 'over_world':
            bg_surf.fill((0, 0, 0))
            dy = height-180
            dx = 0
            if ind == [7,7]:
                scroll_direction[0] = -7
                scroll_direction[1] = 1
            #elif ind == [6,6]:
            #    scroll_direction[0] = -7
            #    scroll_direction[1] = 1
            #elif ind == [5,7]:
            #    scroll_direction[0] = -7
            #    scroll_direction[1] = 1
            #elif ind == [15,6]:
            #    scroll_direction[0] = -7
            #    scroll_direction[1] = 1
            if a:
                player.hitbox.midbottom = (512, 756+dy - 3)
                player.rect.midbottom = player.hitbox.midbottom
                a = False
            if scroll[1] > 0:
                player.hitbox.centery -= scroll_speed
                player.rect.centery -= scroll_speed
                scroll[1] -= scroll_speed
                zy -= scroll_speed
            else:
                ind[0] += scroll_direction[0]
                ind[1] += scroll_direction[1]
                scroll_direction[0] = 0
                scroll_direction[1] = 0
                demention = 'dangeon'
                scroll[1] = 704
                player.enter_stat = False
                a = True
                go_stat = True
                zy = 0
            screen.blit(bg_surf, (dx, height+zy))

        elif demention == 'dangeon':
            bg_surf.fill((252, 216, 168))
            dy = -height + 180
            dx = 0
            if ind == [0,8]:
                scroll_direction[0] = 7
                scroll_direction[1] = -1
            #if ind == [0,8]:
            #    scroll_direction[0] = 7
            #    scroll_direction[1] = -1
            #if ind == [0,8]: 
            #    scroll_direction[0] = 7
            #    scroll_direction[1] = -1
            #if ind == [0,8]:
            #    scroll_direction[0] = 7
            #    scroll_direction[1] = -1
            if a:
                player.hitbox.midbottom = (288, dy + 180 + 192)
                player.rect.midbottom = player.hitbox.midbottom
                a = False
            if scroll[1] > 0:
                player.hitbox.centery += scroll_speed
                player.rect.centery += scroll_speed
                scroll[1] -= scroll_speed
                zy += scroll_speed
            else:
                ind[0] += scroll_direction[0]
                ind[1] += scroll_direction[1]
                scroll_direction[0] = 0
                scroll_direction[1] = 0
                demention = 'over_world'
                scroll[1] = 704
                player.enter_stat = False
                a = True
                go_stat = True
                zy = 0
            screen.blit(bg_surf, (dx, -height+360+zy))
    
    if sotw_direction['N']:
        go_stat = False
        dy = -height + 180
        dx = 0
        if scroll[1] > 0:
            player.hitbox.centery += scroll_speed
            player.rect.centery += scroll_speed
            scroll[1] -= scroll_speed
            zy += scroll_speed
            if player.hitbox.centery >= height:
                player.hitbox.centery = height
                player.rect.centery = height-16
        
        else:
            ind[1] += scroll_direction[1]
            scroll_direction[1] = 0
            scroll[1] = 704
            sotw_direction['N'] = False
            go_stat = True
            zy = 0

    elif sotw_direction['S']:
        go_stat = False
        dy = height-180
        dx = 0
        if scroll[1] > 0:
            player.hitbox.centery -= scroll_speed
            player.rect.centery -= scroll_speed
            scroll[1] -= scroll_speed
            zy -= scroll_speed
            #if player.hitbox.centery <= 180:
            #    player.hitbox.centery = 180
            #    player.rect.centery = 180-36
        
        else:
            ind[1] += scroll_direction[1]
            scroll_direction[1] = 0
            scroll[1] = 704
            sotw_direction['S'] = False
            go_stat = True
            zy = 0

    elif sotw_direction['W']:
        go_stat = False
        dx = -width
        dy = 0
        if scroll[0] > 0:
            player.hitbox.centerx += scroll_speed
            player.rect.centerx += scroll_speed
            scroll[0] -= scroll_speed
            zx += scroll_speed
            if player.rect.centerx >= width:
                player.hitboxcenterx = width
                player.rect.centerx = width
            
        else:
            ind[0] += scroll_direction[0]
            scroll_direction[0] = 0
            scroll[0] = 1024
            sotw_direction['W'] = False
            go_stat = True
            zx = 0

    elif sotw_direction['E']:
        go_stat = False
        dx = width
        dy = 0
        if scroll[0] > 0:
            player.hitbox.centerx -= scroll_speed
            player.rect.centerx -= scroll_speed
            scroll[0] -= scroll_speed
            zx -= scroll_speed
            if player.rect.centerx <= 0:
                player.hitbox.centerx = 0
                player.rect.centerx = 0

        else:
            ind[0] += scroll_direction[0]
            scroll_direction[0] = 0
            scroll[0] = 1024
            sotw_direction['E'] = False
            go_stat = True
            zx = 0

bg = (252, 216, 168)

go_stat = True

sotw_direction = {
    'N': False,
    'S': False,
    'W': False,
    'E': False
    }

scroll = [1024,704]
scroll_direction = [0,0]
ind = [7,7]
scroll_speed = 16

zx = 0
zy = 0

dx = 0
dy = 0

demention = 'over_world'

world = world_map

a = True

enters = {
    'H8':[7, 7],
    'G7':[6, 6],
    'P7':[15, 6],
    'F8':[5, 8]
    }




start_pos = (512, 512)
player = Player(start_pos)
menu = Menu(font30)
uif = Interface()







while True:
    ########################################################
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gamepad.stop_listening()
            pg.quit()
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                menu.switch(-1)
            elif event.key == pg.K_DOWN:
                menu.switch(1)
            elif event.key == pg.K_SPACE:
                menu.game_stat = menu.select()
            elif event.key == pg.K_ESCAPE:
                menu.game_stat = 0
            
    ########################################################
    if demention == 'over_world': bg = (252, 216, 168)
    elif demention == 'dangeon': bg = (0, 0, 0)
    screen.fill(bg)
    ########################################################

    if menu.game_stat != 1:
        if menu.game_stat == 0:
            menu.rendering(width//2, height//2, menu_surf)
        elif menu.game_stat == 'help':
            menu.help(menu_surf)
        elif menu.game_stat == 499:
            pg.quit()
            quit()

        screen.blit(menu_surf, (0, 0))
        pg.display.update()
        clock.tick(FPS)
        continue

    print(ind, player.enter_stat)

    map_scrolling()
    
    map_rendering(world, (ind[0]+scroll_direction[0], ind[1]+scroll_direction[1]), zx+dx, zy+dy)
    map_rendering(world, ind, zx, zy)
    
    player.update(obstacle_sprites, enter_sprites, go_stat)
    screen.blit(player.image, player.rect1)

    ########################################################

    fx, fy = pg.mouse.get_pos()
    #print(fx, fy)

    uif.rendering(ind)
    screen.blit(uif.surf, (0,0))

    ########################################################
    
    if player.keys[pg.K_SLASH]:
        pg.draw.rect(screen, (255, 0, 0), player.rect, 1)
        pg.draw.rect(screen, (255, 0, 0), player.rect1, 1)
        pg.draw.rect(screen, (255, 0, 0), player.hitbox, 1)
        for sprite in obstacle_sprites:
            pg.draw.rect(screen, (255, 0, 0), sprite, 1)

    debug([player.hitbox.midbottom], y = 10, x = 500)
            
    ########################################################
    pg.display.update()
    clock.tick(FPS)

"""
x = 15
y = 15
for i in range((map_rect.height - 10) // 10):
    for i in range((map_rect.width-10) // 10):
        rect = pg.Rect(x, y, 10, 10)
        pg.draw.rect(ui_surf, (255, 0, 0), rect, 1)
        x += 10
    x = 15
    y += 10
"""