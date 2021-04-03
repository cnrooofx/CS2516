"""Adaptable Priority Queue."""

class Element:
    """An Element to store data with an associated key."""

    def __init__(self, key, value, index):
        """Initialise a new element.

        Args:
            key (any): The key associated with the data.
            value (any): The data of the element.
            index (int): The index of the element in a data structure.
        """
        self._key = key
        self._value = value
        self._index = index

    def __eq__(self, other):
        """Return True if this key is equal to the other, otherwise False."""
        return self._key == other._key

    def __lt__(self, other):
        """Return True if this key is less than the other, otherwise False."""
        return self._key < other._key

    def __gt__(self, other):
        """Return True if this key is greater than other, otherwise False."""
        return self._key > other._key

    def _wipe(self):
        """Clear all of the data in the element."""
        self._key = None
        self._value = None
        self._index = None


class AdaptablePQ:
    """Adaptable Priority Queue."""

    def __init__(self):
        """Initialise a new queue."""
        self._heap = []
        self._size = 0

    def length(self):
        """Return the length of the queue."""
        return self._size

    def add(self, key, value):
        """Add an item to the queue with the specified priority.

        Returns:
            A reference to the item within the queue.
        """
        index = self._size
        element = Element(key, value, index)
        self._heap.append(element)
        self._bubbleup(index)
        self._size += 1
        return element

    def get_min(self):
        """Return the highest priority item in the queue.

        Returns:
            The element with the smallest key value.
        """
        if self._size == 0:
            return None
        return self._heap[0]

    def remove(self, element):
        """Remove and return the given element from the queue.

        Args:
            element (Element): An element already in the queue.

        Returns:
            The (key, value) pair from the element.
        """
        index = element._index
        if index >= self._size or self._heap[index] is not element:
            return None
        # Swap the element with the last item in the queue
        self._swap(index, self._size - 1)
        # Remove the last item (now the required element) and update size
        removed_element = self._heap.pop()
        self._size -= 1
        self._rebalance(index)

        key, value = removed_element._key, removed_element._value
        removed_element._wipe()
        return (key, value)
    
    def remove_min(self):
        """Remove and return the highest priority item in the queue.

        Returns:
            The (key, value) pair of the highest priority item.
        """
        min_value = self.get_min()
        if min_value is not None:
            return self.remove(min_value)

    def get_key(self, element):
        """Return the current key for element.

        Args:
            element (Element): An element already in the queue.

        Returns:
            The key of the given element.
        """
        return element._key

    def update_key(self, element, newkey):
        """Update the key of the element."""
        if element._key is not None and element._value is not None:
            element._key = newkey
            index = element._index
            self._rebalance(index)

    def _rebalance(self, i):
        """Rebalance the item at index to the correct position."""
        parent = (i - 1) // 2
        if parent >= 0 and self._heap[i] < self._heap[parent]:
            self._bubbleup(i)
        else:
            self._bubbledown(i)

    def _bubbleup(self, i):
        """Bubble item at index up to its correct position in the heap."""
        parent = (i - 1) // 2
        if parent >= 0 and self._heap[i] < self._heap[parent]:
            self._swap(i, parent)
            self._bubbleup(parent)

    def _bubbledown(self, i):
        """Bubble item at index down to its correct position in the heap."""
        left = 2 * i + 1
        right = 2 * i + 2
        minchild = left
        if right < self._size and self._heap[right] < self._heap[left]:
            minchild = right
        if left < self._size and self._heap[i] > self._heap[minchild]:
            self._swap(i, minchild)
            self._bubbledown(minchild)
    
    def _swap(self, i, j):
        """Swap the two elements at the given indices."""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        self._heap[i]._index = i
        self._heap[j]._index = j


class SearchableAPQ(AdaptablePQ):
    """Searchable Adaptable Priority Queue.

    Has a lookup structure for getting references to items within the queue.
    """

    def __init__(self):
        super().__init__()
        self._lookup = {}
    
    def search(self, item):
        """Get the reference to the item in the queue."""
        try:
            element = self._lookup[item]
        except KeyError:
            element = None
        return element
    
    def add(self, key, value):
        """Add an item to the queue with the specified priority.

        Returns:
            A reference to the item within the queue.
        """
        element = super().add(key, value)
        self._lookup[item] = element
        return element

    def remove(self, element):
        """Remove and return the given element from the queue.

        Args:
            element (Element): An element already in the queue.

        Returns:
            The (key, value) pair from the element.
        """
        removed = super().remove(element)
        del self._lookup[removed[1]]
        return removed
