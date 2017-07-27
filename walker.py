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
        cur_pos = (vertex[0] + self.cur_pos[0])/2, (vertex[1] + self.cur_pos[1])/2
        if not self.structure.check_pos(cur_pos):
            self.walk()
        else:
            self.cur_pos = cur_pos


