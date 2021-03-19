
class Element:
    def __init__(self, key, item):
        self._key = key
        self._element = item
        self._position = 0
    
    def _left(self):
        return 2 * self._position + 1

    def _right(self):
        return 2 * self._position + 2

    def _parent(self):
        return (self._position - 1) // 2

class BinaryHeap:
    def __init__(self):
        self._body = []
    
    def add(self, key, item):
        element = Element(key, item)
