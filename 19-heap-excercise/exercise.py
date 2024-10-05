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

    def _sink_down(self, index):
        max_index = index
        while True:
            left_child = self._left_child(index)
            right_child = self._right_child(index)

            if left_child < len(self.heap) and self.heap[left_child] > self.heap[max_index]:
                max_index = left_child
            
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_index]:
                max_index = right_child

            if max_index is not index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
        
class MinHeap:
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

    def _sink_down(self, index):
        min_index = index
        while True:
            left_child = self._left_child(index)
            right_child = self._right_child(index)

            if left_child < len(self.heap) and self.heap[left_child] < self.heap[min_index]:
                min_index = left_child
            
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[min_index]:
                min_index = right_child

            if min_index is not index:
                self._swap(index, min_index)
                index = min_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_heap = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_heap