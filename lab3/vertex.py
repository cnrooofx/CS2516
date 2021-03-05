"""Class to represent a Vertex as part of a Graph."""

class Vertex:
    def __init__(self, label):
        self._label = label

    def __str__(self):
        return str(self._label)

    @property
    def label(self):
        return self._label