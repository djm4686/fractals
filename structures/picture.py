__author__ = 'dmadden'

from square import Square
import pygame
import random


class Picture(Square):

    def __init__(self, w, h, picture="dickbutt.png"):
        super(Picture, self).__init__(w, h)
        center = w/2, h/2
        self.image = pygame.image.load(picture)
        self.image_h = self.image.get_height()
        self.image_w = self.image.get_width()
        self.center = center
        self.x = center[0] - (self.image_w/2)
        self.y = center[1] - (self.image_h/2)

    def to_local_coords(self, point):
        return point[0] - self.x, point[1] - self.y

    def get_next_vertex(self):
        return random.choice(self.points)

    def check_pos(self, pos):
        local_pos = self.to_local_coords(pos)
        if local_pos[0] < 0 or local_pos[1] < 0:
            return True
        if local_pos[0] > self.image_w-5 or local_pos[1] > self.image_h-5:
            return True
        if self.image.get_at(local_pos)[3] > 200:
            return False
        return True


