
class Element:
    def __init__(self, key, item):
        self._key = key
        self._element = item

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


class MinHeap:
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

    def get_min(self):
        if self._size == 0:
            return None
        return self._body[0]

    def remove_min(self):
        min_value = self.get_min()
        if min_value:
            last_pos = self._size - 1
            self._body[0] = self._body[last_pos]
            del self._body[last_pos]
            self._size -= 1
            self._bubbledown(0)
        return min_value

    def _bubbleup(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self._body[i] < self._body[parent]:
            self._swap(i, parent)
            self._bubbleup(parent)

    def _bubbledown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minchild = left
        if right < self._size and self._body[right] < self._body[left]:
            minchild = right
        if left < self._size and self._body[i] > self._body[minchild]:
            self._swap(i, minchild)
            self._bubbledown(minchild)

    def _swap(self, i, j):
        self._body[i], self._body[j] = self._body[j], self._body[i]
