__author__ = 'dmadden'


class Walker:

    def __init__(self, w, h, structure):
        self.width = w
        self.height = h
        self.structure = structure(w, h)
        self.structure.gen_points()
        self.cur_pos = self.structure.get_inside_point()

    def walk(self):
        vertex = self.structure.get_next_vertex()
        self.cur_pos = (vertex[0] + self.cur_pos[0])/2, (vertex[1] + self.cur_pos[1])/2

