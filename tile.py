import pygame
from pygame.sprite import Group

from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups: Group, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        y_offset = HITBOX_OFFSETS[sprite_type]
        self.sprite_type = sprite_type
        self.image = surface

        if sprite_type == 'object':
            # do an offset
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)

        self.hitbox = self.rect.inflate(-10, y_offset)
