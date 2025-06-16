class NewNode:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self):
        self.item_count = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None
    
    def get_front(self):
        """To print the first element in the deque"""
        if not self.is_empty():
            return self.front.item
        else:
            raise ValueError("Deque is EMPTY")
        
    def get_rear(self):
        """To print the last element from the deque"""
        if not self.is_empty():
            return self.rear.item
        else:
            raise ValueError("Deque is EMPTY")
            
    def front_insertion(self, data):
        """To Insert the element from the front into the deque"""
        node = NewNode(None, data, self.front)
        if not self.is_empty():
            self.front.prev = node
        else:
            self.rear = node
        self.front = node
        self.item_count += 1
    
    def rear_insertion(self, data):
        """To Insert the element from the rear into the deque"""
        node = NewNode(item=data, next=None)
        if not self.is_empty():
            self.rear.next = node
        else:
            self.front = node
        self.rear = node
        self.item_count += 1

    def front_deletion(self):
        """To Delete the element from the front into the deque"""
        try:
            if not self.is_empty():
               self.front = self.front.next
               self.front.prev = None
            elif self.front == self.rear:
               self.front = None
               self.rear = None
            else:
               raise ValueError("Deque is EMPTY")
            self.item_count -= 1
        except Exception as e:
            print(e)

    def rear_deletion(self):
        """To Delete the element from the rear of the deque"""
        try:
            if self.front == self.rear:
               self.front = None
               self.rear = None 
            elif not self.is_empty():
                self.rear.prev = None
                self.rear = self.rear.prev
            else:
               raise ValueError("Deque is EMPTY")
            self.item_count -= 1
        except Exception as e:
            print(e)

    def size(self):
        """To print the size of Deque"""
        return self.item_count

dq = Deque()
dq.rear_insertion(20)
dq.front_insertion(10)
dq.rear_insertion(30)
print("Size of DeQue before deletion operation::", dq.size())
print("Rear Value in the DeQue ::", dq.get_rear())
print("Front Value in the DeQue ::", dq.get_front())
dq.front_deletion()
print("Front Value in the DeQue after deletion operation ::", dq.get_front())
dq.rear_deletion()
print("Rear Value in the DeQue after deletion operation ::", dq.get_rear())
print("Size of DeQue after deletion operation::", dq.size())


