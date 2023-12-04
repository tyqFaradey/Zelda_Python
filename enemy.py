import pygame as pg
from settings import *
from support import *

class Enemy(pg.sprite.Sprite):
    def __init__(self, enemy_name, pos, obstacle_sprites):
        #self.import_sprites(enemy_name)
        self.status = 'down'

        self.image = pg.image.load('images/enemies/octorok/down/octorok1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.frame_index = 0
        self.animation_speed = 0
        self.direction = pg.math.Vector2()

        self.hitbox = self.rect

        self.speed = 3

        


    def move(self, obstacle_sprites, go_stat):
        if go_stat:
            self.hitbox.x += self.direction.x * self.speed
            self.collision('horizontal', obstacle_sprites)
            self.hitbox.y += self.direction.y * self.speed
            self.collision('vertical', obstacle_sprites)
            self.rect.bottom = self.hitbox.bottom
            self.rect.centerx = self.hitbox.centerx
    
    def collision(self, direction, obstacle_sprites):
        if direction == 'horizontal':
            for sprite in obstacle_sprites:
                if sprite.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.right

        if direction == 'vertical':
            for sprite in obstacle_sprites:
                if sprite.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.bottom
    
    def import_sprites(self, name):
        character_path = f'images/enemies/{name}/'
        self.animations = {'up': [pg.image.load('images/enemies/octorok/up/octorok1.png').convert_alpha(), pg.image.load('images/enemies/octorok/up/octorok2.png').convert_alpha()], 
                           'down': [pg.image.load('images/enemies/octorok/down/octorok1.png').convert_alpha(), pg.image.load('images/enemies/octorok/down/octorok2.png').convert_alpha()], 
                           'left': [pg.image.load('images/enemies/octorok/left/octorok1.png').convert_alpha(), pg.image.load('images/enemies/octorok/left/octorok2.png').convert_alpha()], 
                           'right': [pg.image.load('images/enemies/octorok/right/octorok1.png').convert_alpha(), pg.image.load('images/enemies/octorok/right/octorok2.png').convert_alpha()]}

        #for animation in self.animations.keys():
        #    full_path = character_path + animation
        #    self.animations[animation] = import_folder(full_path)

    def get_status(self):
        pass

    def update(self, obstacle_sprites):
        self.move(obstacle_sprites)

