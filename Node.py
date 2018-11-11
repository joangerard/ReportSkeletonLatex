class Node:
    def __init__(self):
        self._value = None
        self._right = None
        self._left = None

    def add_rigth(self, node):
        self._right = node

    def add_left(self, node):
        self._left = node

    def add_value(self, value):
        self._value = value

    def has_children(self):
        return self._right is not None or self._left is not None

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_value(self):
        return self._value
