class PriorityQueue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    
    def push(self, priority, data):
        """To Add the data on the priority basis in the Queue"""
        index = 0
        while index < len(self.item) and self.item[index][1] <= priority:
              index += 1
        self.item.insert(index, (data, priority))

    def pop(self):
        """To Remove the Top Priority Data from Queue"""
        if not self.is_empty():
           self.item.pop(0)
        else:
            raise IndexError("Queue is EMPTY")
        
    def size(self):
        return len(self.item)

pq = PriorityQueue()
pq.push(1, 20)
pq.push(2, 30)
pq.push(0, 10)
print("Size of Priority Queue before Pop Operation ::", pq.size())
pq.pop()
print("Size of Priority Queue after Pop Operation ::", pq.size())
