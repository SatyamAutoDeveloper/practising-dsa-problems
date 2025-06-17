import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from LinkedList.doubly_linked_lists import *

class Deque:
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.item_count = 0

    def is_empty(self):
        return self.dll.is_empty()
    
    def get_front(self):
        """To print the first element in the deque"""
        if not self.is_empty():
            return self.dll.start.item 
        else:
            raise ValueError("DeQUE is EMPTY")
        
    def get_rear(self):
        """To print the last element from the deque"""
        if not self.is_empty():
            temp = self.dll.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise ValueError("Deque is EMPTY")
        
    def front_insertion(self, data):
        """To Insert the Data from Front into the DeQue"""
        self.dll.insert_node_at_start(data)
        self.item_count += 1

    def rear_insertion(self, data):
        """To Insert the Data from Rear into the DeQue"""
        self.dll.insert_node_at_end(data)
        self.item_count += 1
    
    def front_deletion(self):
        """To Delete the Data from Front of the DeQue"""
        if not self.is_empty():
            self.dll.delete_node_from_start()
            self.item_count -= 1
        else:
            raise ValueError("Deque is EMPTY")

    def rear_deletion(self):
        """To Delete the Data from Rear of the DeQue"""
        if not self.is_empty():
            self.dll.delete_node_from_last()
            self.item_count -= 1
        else:
            raise ValueError("Deque is EMPTY")

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
