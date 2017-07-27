__author__ = 'dmadden'

from fractal_structure import FractalStructure
import random

class Square(FractalStructure):

    def __init__(self,w, h):
        super(Square, self).__init__(w, h)
        self.cur_vertex = None

    def gen_points(self):
        p1 = 0, 0
        p2 = self.width, 0
        p3 = 0, self.height
        p4 = self.width, self.height
        self.points = [p1, p2, p3, p4]
        self.cur_vertex = p1

    def get_next_vertex(self):
        maybe_next = random.choice(self.points)
        while maybe_next == self.cur_vertex:
            maybe_next = random.choice(self.points)
        self.cur_vertex = maybe_next
        return maybe_next

    def get_inside_point(self):
        return self.width/2, self.height/2