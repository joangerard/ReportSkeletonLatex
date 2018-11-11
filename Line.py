class Line:
    def __init__(self, m, b):
        """
        y = mx + b
        :param m: float
        :param b: float
        """
        self.m = m
        self.b = b

    def calculate_y(self, x):
        """
        Calculate y given x
        :param x: float
        :return:
        """
        return self.m * x + self.b