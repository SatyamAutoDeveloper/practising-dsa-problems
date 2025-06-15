class Queue(list):
    def __init__(self):
        self.item_count = 0

    def is_empty(self):
        return len(self) == 0
    
    def get_front(self):
        """To Display the 1st entered value into the Queue"""
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("Queue is EMPTY")
        
    def get_rear(self):
        """To Display the Last Entered value into the Queue"""
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Queue is EMPTY")
        
    def enqueue(self, data):
        """To Insert the data into the Queue"""
        self.append(data)
        self.item_count += 1

    def dequeue(self):
        """To remove the 1st inserted data from the Queue"""
        if not self.is_empty():
           first_val = self.get_front()
           self.remove(first_val)
           self.item_count -= 1
        else:
            raise ValueError("This f{first_val} is not found in Queue")
        return first_val
    
    def size(self):
        """To Display Total Count of the Elements inside the Queue"""
        return self.item_count
    
    def pop(self):
        """Overriding of list pop function to restrict its use into the Queue"""
        try:
           if not self.is_empty():
               raise AttributeError("No 'pop' function in Queue")
        except Exception as e:
            print(e)

    def insert(self, index, value):
        """Overriding of list insert function to restrict its use into the Queue"""
        try:
           if not self.is_empty():
               raise AttributeError("No 'insert' function in Queue")
        except Exception as e:
            print(e)

    
    
qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
print("Size of Queue before dequeue operation::", qu.size())
print("Last Value in the Queue ::", qu.get_rear())
print("Dequeue First Entered value from the Queue ::", qu.dequeue())
print("Size of Queue after dequeue operation::", qu.size())
qu.pop()
qu.insert(0, 40)
print("First Value in the Queue after dequeue operation ::", qu.get_front())