class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 or self.heap[current] > self.heap[self._parent(current)]:
            self._swap(0, self.parent(current))
            current = self._parent(current)