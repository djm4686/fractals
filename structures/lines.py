__author__ = 'dmadden'


from fractal_structure import FractalStructure


class Lines(FractalStructure):

    def __init__(self, w, h):
        super(Lines, self).__init__(w, h)
        p1 = 100, 100
        p2 = w - 100, 100
        p3 = w/2, h-100
        line1 = lambda x: ((p1[1] - p3[1])/(p1[0] - p3[0]))*x
        line2 = lambda x: ((p2[1] - p3[1])/(p2[0] - p3[0]))*x


    def gen_points(self):
        pass