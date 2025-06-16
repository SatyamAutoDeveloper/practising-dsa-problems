"""DeQue:  Doubly Ended Queue"""

class Deque:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    
    def get_front(self):
        """To print the first element in the deque"""
        try:
            if not self.is_empty():
                return self.item[0]
            else:
                raise IndexError("Deque is EMPTY")
        except Exception as e:
            print(e)

    def get_rear(self):
        """To print the last element in the deque"""
        try:
            if not self.is_empty():
                return self.item[-1]
            else:
                raise IndexError("Deque is EMPTY")
        except Exception as e:
            print(e)

    def front_insertion(self, data):
        """To insert the data from the front into the Deque"""
        self.item.insert(0, data)

    def rear_insertion(self, data):
        """To insert the data from rear into the Deque"""
        self.item.append(data)

    def front_deletion(self):
        """To delete the data from the front of the Deque"""
        try:
            if not self.is_empty():
                self.item.pop(0)
            else:
                raise IndexError("Deque is EMPTY")
        except Exception as e:
            print(e)

    def rear_deletion(self):
        """To delete the data from rear of the Deque"""
        try:
            if not self.is_empty():
                self.item.pop(-1)
            else:
                raise IndexError("Deque is EMPTY")
        except Exception as e:
            print(e)

    def size(self):
        return len(self.item)

        
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
