__author__ = 'dmadden'


from fractal_structure import FractalStructure


class Triangle(FractalStructure):

    def __init__(self, width, height):
        super(Triangle, self).__init__(width, height)

    def gen_points(self, random=False):
        self.points = []
        if random:
            for _ in range(3):
                self.points.append(self.get_random_point())
        else:
            p1 = self.width/2, 10
            p2 = 10, self.height-10
            p3 = self.width-10, self.height-10
            self.points = [p1, p2, p3]

    def get_inside_point(self):
        p1 = self.points[0]
        p2 = self.points[1]
        p3 = self.points[2]
        return (p1[0] + p2[0] + p3[0])/3, (p1[1] + p2[1] + p3[1])/3