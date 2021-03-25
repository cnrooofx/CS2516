
class Element:
    def __init__(self, key, item):
        self._key = key
        self._element = item
        self._position = 0
    
    def __str__(self):
        return "({}, {})".format(self._key, self._element)
    
    def __eq__(self, other):
        return self._key == other.key

    def __lt__(self, other):
        return self._key < other.key

    def __gt__(self, other):
        return self._key > other.key

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value
class BinaryHeap:
    def __init__(self):
        self._body = []
        self._size = 0
    
    def size(self):
        return self._size
    
    def add(self, key, item):
        element = Element(key, item)
        self._body.append(element)
        self._bubbleup(self._size)
        self._size += 1

    def _bubbleup(self, i):
        parent = (i - 1) // 2
        if self._body[i] < self._body[parent]:
            self._swap(i, parent)
            self._bubbleup(parent)

    def _swap(self, i, j):
        self._body[i], self._body[j] = self._body[j], self._body[i]
