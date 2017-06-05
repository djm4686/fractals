__author__ = 'dmadden'
import random


class FractalStructure(object):

    def __init__(self, width, height):
        self.points = []
        self.width = width
        self.height = height

    def get_point(self):
        return self.points[random.randrange(0, len(self.points))]

    def gen_points(self):
        self.points = []

    def get_random_point(self):
        return (random.randrange(0, self.width), random.randrange(0, self.height))

    def get_next_vertex(self):
        return random.choice(self.points)