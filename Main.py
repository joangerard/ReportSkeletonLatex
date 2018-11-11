from Segment import Segment
from Point import Point
from BSPManager import BSPManager
from Graphic import Graphic
import itertools
import sys


class Main:
    def __init__(self):
        self.bsp = BSPManager()

    def extract_segments_from_file(self):
        """
        It reads the segments from a file with the follow structure:
        x1, y1, x2, y2, name
        :return: list
        """
        segments = []
        file_name = 'test_samples.txt'
        if len(sys.argv) > 1:
            file_name = sys.argv[1]
        file = open(file_name, 'r')
        for line in file:
            points = line.split(' ')
            point_start = Point(float(points[0]), float(points[1]))
            point_end = Point(float(points[2]), float(points[3]))
            name = points[4].replace('\n', '')
            segments.append(Segment(point_start, point_end, name))
        return segments

    def execute(self):
        """
        It generates all the possible permutations given a set of
        segments and saves it into a list called list_permuted_segments
        then it builds the BSP tree for each set of segments and calculates
        its size.

        I
        :return: list, dictionary
        """
        i = 0
        sizes = []
        segments = self.extract_segments_from_file()
        segment_classifier_size = {}

        # Get all possible permutations of the segments
        list_permuted_segments = itertools.permutations(segments)

        for set_segments in list_permuted_segments:
            bsp = self.bsp.build(list(set_segments))
            size = self.bsp.size(bsp)
            sizes.append(size)

            # if it is the first time it reads this size
            if size not in segment_classifier_size:
                segment_classifier_size[size] = []

            # it saves a record of the BSP tree size obtained
            # given the first segment selected from the permutation
            segment_classifier_size[size].append(bsp.get_value().name)
            i += 1
        return sizes, segment_classifier_size

    def execute_once(self):
        """
        Executes the BSP algorithm for a given set of segments.
        """
        segments = self.extract_segments_from_file()
        bsp = self.bsp.build(list(segments))
        print('Size of BSP tree: %i' % self.bsp.size(bsp))


main = Main()
graphic = Graphic()
segments = main.extract_segments_from_file()
main.execute_once()
sizes, segment_classifier_size = main.execute()

graphic.graphic(segments, sizes, segment_classifier_size)

