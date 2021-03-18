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
        """Return the pair of vertices in the edge."""
        return (self._v1, self._v2)
    
    def start(self):
        """Return the first vertex in the ordered pair."""
        return self._v1

    def end(self):
        """Return the second vertex in the ordered pair."""
        return self._v2

    def opposite(self, vertex):
        if vertex == self._v1:
            return self._v2
        elif vertex == self._v2:
            return self._v1
        return None
