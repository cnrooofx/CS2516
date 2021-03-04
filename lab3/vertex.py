"""Class to represent a Vertex as part of a Graph."""

class Vertex:
    def __init__(self, label):
        self._label = label

    def __str__(self):
        return str(self._label)

    def element(self):
        return self._label
