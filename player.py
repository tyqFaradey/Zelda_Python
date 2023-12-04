import pygame as pg
from support import import_folder

class Player(pg.sprite.Sprite):
    def __init__(self, start_pos):
        self.image = pg.image.load('images/player/down/player1f.png').convert_alpha()
        self.rect = self.image.get_rect(midtop=start_pos)
        self.hitbox = self.rect.inflate(-20, -36)

        self.import_player_asssets()
        self.status = 'down'

        self.attaking = False
        self.attak_cooldown = 400
        self.attack_anim_speed = 0.08
        self.attak_time = None

        self.frame_index = 0
        self.animation_speed = 0.1 
        self.cache_index = 0

        self.keys = None

        self.direction = pg.math.Vector2()
        self.speed = 2

        self.enter_stat = False

    def import_player_asssets(self):
        character_path = 'images/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [], 
                'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
        
    def get_status(self):

        #idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status += '_idle'

        if self.attaking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status += '_attack'

        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def input(self):

        # movement input
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_w]:
            self.direction.y = -1
            self.direction.x = 0
            if not '_attack' in self.status:
                self.status = 'up'
        elif self.keys[pg.K_s]:
            self.direction.y = 1
            self.direction.x = 0
            if not '_attack' in self.status:
                self.status = 'down'
        elif self.keys[pg.K_a]:
            self.direction.x = -1
            self.direction.y = 0
            if not '_attack' in self.status:
                self.status = 'left'
        elif self.keys[pg.K_d]:
            self.direction.x = 1
            self.direction.y = 0
            if not '_attack' in self.status:
                self.status = 'right'

        else:
            self.direction.x = 0
            self.direction.y = 0

        #attack input
        if self.keys[pg.K_x] and not self.attaking:
            self.attaking = True
            self.attak_time = pg.time.get_ticks()

    def move(self, obstacle_sprites, go_stat):
        if go_stat:
            self.hitbox.x += self.direction.x * self.speed
            self.collision('horizontal', obstacle_sprites)
            self.hitbox.y += self.direction.y * self.speed
            self.collision('vertical', obstacle_sprites)
            self.rect.midbottom = self.hitbox.midbottom
            #self.rect.centerx = self.hitbox.centerx
    
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

    def dang_enter(self, enter_sprites):
        for rect in enter_sprites:
            if rect.colliderect(self.hitbox):
                self.enter_stat = True

    def cooldowns(self):
        current_time = pg.time.get_ticks()

        if self.attaking:
            if current_time - self.attak_time >= self.attak_cooldown:
                self.attaking = False

    def animate(self):
        animation = self.animations[self.status]
        if '_attack' in self.status:
            self.animation_speed = self.attack_anim_speed
            if self.frame_index >= len(animation):
                self.attaking = False

        self.frame_index += self.animation_speed
        
        if self.frame_index >= len(animation):
            self.frame_index = 0
        

        self.image = animation[int(self.frame_index)]
        self.rect1 = pg.Rect((self.rect.topleft), self.image.get_size())

        if self.status == 'left_attack':
            self.rect1.right = self.rect.right
        if self.status == 'up_attack':
            self.rect1.bottom = self.rect.bottom

    def update(self, obstacle_sprites, enter_sprites, go_stat):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.dang_enter(enter_sprites)
        self.move(obstacle_sprites, go_stat)