import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LinkedList.singly_linked_lists import *

class Stack():
    def __init__(self):
        self.sll = SinglyLinkedList()
        self.item_count = 0

    def is_empty(self):
        return self.sll.is_empty()
    
    def push(self, data):
        """To push the data into the stack"""
        self.sll.insert_node_at_start(data)
        self.item_count += 1

    def pop(self):
        """To pop the top item from the stack"""
        if not self.is_empty():
            data = self.sll.start.item
            self.sll.delete_node_from_start()
            self.item_count -= 1
        else:
            raise IndexError("Stack is EMPTY")
        return data

    def peek(self):
        """To display the top item from the stack"""
        if not self.is_empty():
            return self.sll.start.item
        else:
            raise IndexError("Stack is EMPTY")

    def size(self):
        """To display the total size of the stack"""
        return self.item_count


st = Stack()
st.push(10)
st.push(20)
st.push(30) 
print("Size of Stack before pop operation::", st.size())
print("Top Value in the Stack ::",st.peek())
print("pop top value from the Stack ::",st.pop())
print("Size of Stack after pop operation::", st.size())
print("Top Value in the Stack ::",st.peek())