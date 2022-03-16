import pygame
from pygame.sprite import Group

from entity import Entity
from player import Player
from settings import *
from support import import_folder


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups: Group, obstacle_sprites):
        # general setup
        super(Enemy, self).__init__(groups)
        self.animations = None
        self.sprite_type = 'enemy'

        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index].convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        # movement
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        main_path = f'./graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self, player: Player):
        # distance =
        # return (distance, direction)
        pass

    def get_status(self, player: Player):
        distance = 0

        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def update(self) -> None:
        self.move(self.speed)
        

