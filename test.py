import pygame

tile_size = 40
pygame.init()
size = [1280, 720]
CELL_SIZE = [40, 40]
FPS = 60
window = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Sokoban")

wall = pygame.transform.scale(pygame.image.load("images/border.png"), CELL_SIZE)
kalitka = pygame.transform.scale(pygame.image.load("images/borderB.png"), CELL_SIZE)
T_sand = pygame.transform.scale(pygame.image.load("images/drev.png"), CELL_SIZE)
F_sand = pygame.transform.scale(pygame.image.load("images/drevB.png"), CELL_SIZE)
P_grass = pygame.transform.scale(pygame.image.load("images/engl.png"), CELL_SIZE)
grass = pygame.transform.scale(pygame.image.load("images/engl1.png"), CELL_SIZE)
rock = pygame.transform.scale(pygame.image.load("images/engl3.png"), CELL_SIZE)
player = pygame.transform.scale(pygame.image.load("images/engl4.png"), CELL_SIZE)

file_name = "карта.txt"

def read_file(file_name):
    map_list = []

    file = open(file_name, 'r')
    for i in range(0, 10):
        s = file.readline()
        arr = s.split()
        map_list.append(arr)
    file.close()
    return map_list


m = read_file(file_name)
for i in m:
    print(i)

def draw_maze(map_list):
    for indi, i in enumerate(map_list):
        for indj, j in enumerate(i):
            x = tile_size * indj
            y = tile_size * indi
            rect = pygame.Rect(x, y, tile_size, tile_size)
            match j:
                case '1':
                    window.blit(wall, rect)
                case '2':
                    window.blit(grass, rect)
                    
def next_step(event, player_row, player_col):
    next_row, next_col = player_row, player_col
    if event.key == pygame.K_w:
        if player_row > 0:
            next_row = player_row - 1
    elif event.key == pygame.K_s:
        if player_row < 22:
            next_row = player_row + 1
    elif event.key == pygame.K_a:
        if player_col > 0:
            next_col = player_col - 1
    elif event.key == pygame.K_d:
        if player_col < 22:
            next_col = player_col + 1
    return next_row, next_col

def move(map_list, player_row, player_col, next_row, next_col):
    if map_list[next_row][next_col] == 1 or map_list[next_row][next_col]==6:
        next_row = player_row
        next_col = player_col
    elif map_list[next_row][next_col] == 2 or map_list[next_row][next_col]==3:
        map_list[next_row][next_col] = 5
        map_list[player_row][player_col] = 2
        player_row = next_row
        player_col = next_col
    return player_row, player_col, next_row, next_col


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            next_row, next_col = next_step(event, player_row, player_col)
            player_row, player_col, next_row, next_col, score, game_win = move(m, player_row, player_col,
                                                                                   next_row, next_col)
    window.fill([170, 115, 60])
        
    draw_maze(m)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
