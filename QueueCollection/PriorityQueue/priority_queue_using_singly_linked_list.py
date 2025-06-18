class NewNode:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self, start=None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self, priority, data):
        """To Add the data on the priority basis in the Queue"""
        node = NewNode(data, priority)
        if self.is_empty() or self.start.priority > priority:
            node.next = self.start
            self.start = node
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            node.next = temp.next
            temp.next = node
            
        self.item_count += 1
            
    def pop(self):
        """To Remove the Top Priority Data from Queue"""
        if not self.is_empty():
            data = self.start.item
            priority = self.start.priority
            self.start = self.start.next
            self.item_count -= 1
        else:
            raise IndexError("Priority Queue is EMPTY")
        return priority, data

    def size(self):
        """To print the size of queue"""
        return self.item_count

pq = PriorityQueue()
pq.push(1, 20)
pq.push(2, 30)
pq.push(3, 10)
print("Size of Priority Queue before Pop Operation ::", pq.size())
print("Data and Priority ::",pq.pop())
print("Size of Priority Queue after Pop Operation ::", pq.size()) 

