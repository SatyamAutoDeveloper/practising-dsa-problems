class HeapSort:
    def __init__(self, nums):
        self.nums = nums
        self.heap = []

    def compare_and_add_value(self, idx, num):
        self.heap.append(num)
        current = idx
        while current > 0:
            rootidx = (current - 1) // 2
            if self.heap[rootidx] < self.heap[current]:
                self.heap[rootidx], self.heap[current] = self.heap[current], self.heap[rootidx]
                current = rootidx
            else:
                break

    def create_heap(self):
        """To create heap from a given list"""
        for idx, num in enumerate(self.nums):
            self.compare_and_add_value(idx, num)
        return self.heap
    
    def insert_value_in_heap(self, num):
        """To insert data in heap"""
        idx = len(self.heap)
        self.compare_and_add_value(idx, num)
        return self.heap
    
    def top_value_in_heap(self):
        """To print the top/max value in the heap"""
        if not self.heap:
            raise IndexError("Heap is empty, cannot delete top value.")
        return self.heap[0]
    
    def delete_top_value_from_heap(self):
        """To delete the top value from the heap and maintain the heap"""
        if not self.heap:
            raise IndexError("Heap is empty, cannot delete top value.")
        top_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            idx = 0
            n = len(self.heap)
            while True:
                left = 2 * idx + 1
                right = 2 * idx + 2
                largest = idx
                if left < n and self.heap[left] > self.heap[largest]:
                    largest = left
                if right < n and self.heap[right] > self.heap[largest]:
                    largest = right
                if largest != idx:
                    self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
                    idx = largest
                else:
                    break
        return top_val
    
    def sort_the_heap(self):
        """To sort the heap"""
        sorted_heap = []
        for _ in range(len(self.heap)):
            sorted_heap.append(self.delete_top_value_from_heap())
        return sorted_heap

hs = HeapSort([32,20,18,70,60,39,75,90,65])
hs.create_heap()
hs.insert_value_in_heap(40)
print("Top value in the heap ::", hs.top_value_in_heap())
#print("Top Deleted Value ::", hs.delete_top_value_from_heap())
print("Sorted List using Heap Sort ::", hs.sort_the_heap())