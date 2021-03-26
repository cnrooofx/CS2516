"""Adaptable Priority Queue."""

class Element:
    def __init__(self, key, value, index):
        self._key = key
        self._value = value
        self._index = index

    def __str__(self):
        return "({}, {})".format(self._key, self._value)

    def __eq__(self, other):
        return self._key == other.get_key()

    def __lt__(self, other):
        return self._key < other.get_key()

    def __gt__(self, other):
        return self._key > other.get_key()

    def get_key(self):
        return self._key

    def get_value(self):
        return self._value
    
    def get_index(self):
        return self._index

    def set_index(self, i):
        self._index = i
    
    def wipe(self):
        self._key = None
        self._value = None
        self._index = None


class AdaptablePQ:
    """Adaptable Priority Queue.
    
    The smallest key value has the highest priority.
    """

    def __init__(self):
        """Initialise a new queue."""
        self._heap = []
        self._size = 0

    def add(self, key, item):
        index = self._size
        element = Element(key, item, index)
        self._heap.append(element)
        self._bubbleup(index)
        self._size += 1
        return element

    def get_min(self):
        """Return the highest priority item in the queue."""
        if self._size == 0:
            return None
        return self._heap[0]

    def remove_min(self):
        """Remove and return the highest priority item in the queue."""
        min_value = self.get_min()
        if min_value is None:
            return None

        last_pos = self._size - 1
        self._heap[0] = self._heap[last_pos]
        del self._heap[last_pos]
        self._size -= 1
        self._bubbledown(0)

        key, value = min_value.get_key(), min_value.get_value()
        return (key, value)

    def remove(self, element):
        """Remove and return the given element from the queue."""
        index = element.get_index()
        self._swap(index, self._size - 1)
        parent = (index - 1) // 2
        if self._heap[index] < self._heap[parent]:
            self._bubbleup(index)
        else:
            self._bubbledown(index)
        removed = self._heap.pop(-1)
        key, value = removed.get_key(), removed.get_value()
        return (key, value)

    def length(self):
        """Return the length of the queue."""
        return self._size
    
    def _bubbleup(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self._heap[i] < self._heap[parent]:
            self._swap(i, parent)
            self._bubbleup(parent)

    def _bubbledown(self, i, last=None):
        if not last:
            last = self._size
        left = 2 * i + 1
        right = 2 * i + 2
        minchild = left
        if right < last and self._heap[right] < self._heap[left]:
            minchild = right
        if left < last and self._heap[i] > self._heap[minchild]:
            self._swap(i, minchild)
            self._bubbledown(minchild)
    
    def _swap(self, i, j):
        """Swap the two elements at the given indices."""
        index_i = self._heap[i].get_index()
        index_j = self._heap[j].get_index()
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        self._heap[i].set_index(index_j)
        self._heap[j].set_index(index_i)
