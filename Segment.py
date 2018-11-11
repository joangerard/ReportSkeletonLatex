from Point import Point
from Line import Line


class Segment:
    def __init__(self, start, end, name='R'):
        """
        given 2 points
        :param start: Point
        :param end:   Point
        """
        self.start = start
        self.end = end
        self.name = name

    def line_projection(self):
        """
        y = mx + b
        :return: Line
        """
        epsilon = 8e-7
        m = (self.end.y - self.start.y)/(self.end.x - self.start.x + epsilon)
        b = self.end.y - m * self.end.x
        return Line(m, b)

    def cut_to(self, point):
        """
        Cuts segment from origin to the point
        :param point: Point
        :return: Segment
        """
        return Segment(self.start, point)

    def cut_from(self, point):
        """
        Cuts segment from point to the end
        :param point: Point
        :return: Segment
        """
        return Segment(point, self.end)
