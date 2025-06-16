class NewNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def get_front(self):
        """To Display the first entered element into the Queue"""
        try:
            if not self.is_empty():
                return self.start.item
            else:
                raise ValueError("Queue is EMPTY")
        except Exception as e:
            print(e)
    
    def get_rear(self):
        """To Display the Last Entered value into the Queue"""
        try:
            temp = self.start
            if not self.is_empty():
                while temp.next is not None:
                    temp = temp.next
                return temp.item
            else:
                raise ValueError("Queue is EMPTY")
        except Exception as e:
            print(e)
    
    def enqueue(self, data):
        """To Insert the data into the Queue"""
        node = NewNode(data, None)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node
        self.item_count += 1

    def dequeue(self):
        """To remove the 1st inserted data from the Queue"""
        if not self.is_empty():
           first_val = self.get_front()
           self.start = self.start.next
           self.item_count -= 1
        else:
            raise ValueError("This f{first_val} is not found in Queue")
        return first_val
    
    def size(self):
        """To Display Total Count of the Elements inside the Queue"""
        return self.item_count


qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
print("Size of Queue before dequeue operation::", qu.size())
print("Last Value in the Queue ::", qu.get_rear())
print("Dequeue First Entered value from the Queue ::", qu.dequeue())
print("Size of Queue after dequeue operation::", qu.size())
print("First Value in the Queue after dequeue operation ::", qu.get_front())