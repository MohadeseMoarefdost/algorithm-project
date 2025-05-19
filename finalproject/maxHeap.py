from binarySearchTree import BST

class HeapNode:
    def __init__(self, id, priority):
        self.priority = priority
        self.id = id

class MaxHeap:
    def __init__(self):
        self.heap = [None]
        self.heap_size = 0

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i
    
    def right(self, i):
        return 2 * i + 1

    def deleteMaxHeap(self):
        if self.heap_size == 0:
            return None
        node = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.heap_size -= 1
        self.maxHeapify(1)
        return node

    def maxHeapify(self, i):
        left = self.left(i)
        right = self.right(i)
        largest = i
        if left <= self.heap_size and self.heap[left].priority > self.heap[right].priority:
            largest = left
        if right <= self.heap_size and self.heap[right].priority > self.heap[largest].priority:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def isEmptyHeap(self):
        return self.heap_size == 0

    def sizeMaxHeap(self):
        return self.heap_size

    def searchP(self, id):
        for i in range(1, len(self.heap)):
            if self.heap[i].id == id:
                return i
        return None
    
    def increasePriority(self, id, newPriority):
        index = self.searchP(id)
        if index is None:
            return
        if newPriority < self.heap[index].priority:
            print("New priority is lower than current priority")
            return
        self.heap[index].priority = newPriority
        while index > 1 and self.heap[self.parent(index)].priority < self.heap[index].priority:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def insertHeap(self, id, priority):
        new_node = HeapNode(id, float('-inf'))
        self.heap.append(new_node)
        self.heap_size += 1
        self.increasePriority(id, priority)
        
    def printMaxHeap(self):
        for i in range(len(self.heap)):
            print(f'id: {self.heap[i].id}   priority: {self.heap[i].priority}')

    def processHighestPriorityRequest(self, bst: BST):
        if self.heap_size == 0:
            return None
        high_priority = self.heap[1].id
        self.deleteMaxHeap()
        bst.deleteRequest(high_priority)
        return high_priority