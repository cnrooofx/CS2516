"""Min and Max Binary Heaps."""

class _BinaryHeap:
    """Base Binary Heap."""

    def __init__(self):
        """Initialise a new Heap."""
        self._body = []
        self._size = 0

    def size(self):
        """Return the size of the heap."""
        return self._size

    def add(self, item):
        """Add item to the heap."""
        self._body.append(item)
        self._bubbleup(self._size)
        self._size += 1

    def _swap(self, i, j):
        """Swap the two items at the given indices."""
        self._body[i], self._body[j] = self._body[j], self._body[i]

class MinHeap(_BinaryHeap):
    """Minimum Binary Heap with smallest value at the top."""

    def __init__(self):
        """Initialise a new Min Heap."""
        super().__init__()

    def get_min(self):
        """Return the smallest value in the heap."""
        if self._size == 0:
            return None
        return self._body[0]

    def remove_min(self):
        """Remove and return the smallest value in the heap."""
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


class MaxHeap(_BinaryHeap):
    """Maximum Binary Heap with largest value at the top."""

    def __init__(self):
        """Initialise a new Max Heap."""
        super().__init__()

    def get_max(self):
        """Return the largest value in the heap."""
        if self._size == 0:
            return None
        return self._body[0]

    def remove_max(self):
        """Remove and return the largest value in the heap."""
        min_value = self.get_max()
        if min_value:
            last_pos = self._size - 1
            self._body[0] = self._body[last_pos]
            del self._body[last_pos]
            self._size -= 1
            self._bubbledown(0)
        return min_value

    def _bubbleup(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self._body[i] > self._body[parent]:
            self._swap(i, parent)
            self._bubbleup(parent)

    def _bubbledown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minchild = left
        if right < self._size and self._body[right] > self._body[left]:
            minchild = right
        if left < self._size and self._body[i] < self._body[minchild]:
            self._swap(i, minchild)
            self._bubbledown(minchild)
