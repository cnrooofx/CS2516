"""Class to represent an Edge between two vertices in a Graph."""

class Edge:
    def __init__(self, label, v1, v2):
        self._label = label
        self._v1 = v1
        self._v2 = v2

    def __str__(self):
        return "Edge {}: {} --- {}".format(self._label, self._v1, self._v2)

    def element(self):
        return self._label

    def vertices(self):
        pass

    def opposite(self, vertex):
        pass
