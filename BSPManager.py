from Node import Node
from Point import Point


class BSPManager:

    def build(self, segments):
        """
        It calls the recursive method.
        :param segments: list
        :return: Node
        """
        binary_tree = self._build_bsp_recursive(segments)
        return binary_tree

    def _build_bsp_recursive(self, segments):
        """
        It builds the BSP tree recursively.
        :param segments: list
        :return: Node
        """
        # node is empty/null
        if len(segments) == 0:
            return None
        # there is only one segment
        if len(segments) == 1:
            leaf = Node()
            leaf.add_value(segments.pop())
            return leaf
        # there are some segments to be processed
        else:
            up_segments = []
            down_segments = []
            segment_separator = segments.pop(0)
            for segment in segments:
                comparison_result = self._compare(segment_separator, segment)
                # segment is above the line separator
                if comparison_result == 'up':
                    up_segments.append(segment)
                # segment is below the line separator
                elif comparison_result == 'down':
                    down_segments.append(segment)
                # segment intersects the line separator
                elif comparison_result == 'between':
                    y1, y2 = self._get_y_pos_based_on(segment_separator, segment)
                    intersection_point = self._get_intersection_point(segment_separator, segment)
                    # cut the segment in two and put one part
                    # into the up list segments and the other into the
                    # down list segment.
                    if y1 < segment.start.y and y2 > segment.end.y:
                        segment_a = segment.cut_to(intersection_point)
                        segment_b = segment.cut_from(intersection_point)
                        up_segments.append(segment_a)
                        down_segments.append(segment_b)
                    elif y1 > segment.start.y and y2 < segment.end.y:
                        segment_a = segment.cut_to(intersection_point)
                        segment_b = segment.cut_from(intersection_point)
                        up_segments.append(segment_b)
                        down_segments.append(segment_a)
            # Recursive call
            right_node = self._build_bsp_recursive(up_segments)
            left_node = self._build_bsp_recursive(down_segments)

            # Node creation
            root = Node()
            root.add_value(segment_separator)
            root.add_left(left_node)
            root.add_rigth(right_node)
            return root

    def _compare(self, segment, to_segment):
        """
        Upper-down calculation between segments.
        :param segment:     Segment
        :param to_segment:  Segment
        :return:            string
        """
        y1, y2 = self._get_y_pos_based_on(segment, to_segment)

        """to_segment is up to the segment"""
        if to_segment.start.y > y1 and to_segment.end.y > y2:
            return 'up'
        elif to_segment.start.y < y1 and to_segment.end.y < y2:
            return 'down'
        else:
            return 'between'

    def _get_y_pos_based_on(self, segment, to_segment):
        """
        Calculate position of to_segment relative to segment.
        :param segment:     Segment
        :param to_segment:  Segment
        :return: int, int
        """
        line_separator = segment.line_projection()
        y1 = line_separator.calculate_y(to_segment.start.x)
        y2 = line_separator.calculate_y(to_segment.end.x)
        return y1, y2

    def _get_intersection_point(self, segment, to_segment):
        """
        Calculate intersection of segment with the line projection.
        :param segment:     Segment
        :param to_segment:  Segment
        :return: Point
        """
        line1 = segment.line_projection()
        line2 = to_segment.line_projection()
        x = (line1.b - line2.b) / (line2.m - line1.m)
        y = line1.m * x + line1.b
        return Point(x, y)

    def size(self, bsp):
        """
        Call the recursive call that calculates the size of the tree.
        :param bsp: Node
        :return: int
        """
        return self._size(bsp, 0)

    def _size(self, node, counter):
        """
        Calculates the size of the tree.
        :param node: Node root node at the very first call
        :param counter: int
        :return:
        """
        # Node is empty, do nothing.
        if node is None:
            return counter
        # It is a leaf
        if not node.has_children():
            return counter + 1
        # Recursive calls
        else:
            counter = self._size(node.get_left(), counter)
            counter = self._size(node.get_right(), counter)
            return counter + 1
