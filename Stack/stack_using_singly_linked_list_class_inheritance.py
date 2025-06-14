import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LinkedList.singly_linked_lists import *

class Stack(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        """To push the data in the stack"""
        self.insert_node_at_start(data)
        self.item_count += 1

    def pop(self):
        """To Remove the Top item from the stack"""
        if not self.is_empty():
            data = self.start.item
            self.delete_node_from_start()
            self.item_count -= 1
        else:
            raise IndexError("Stack is EMPTY")
        return data

    def peek(self):
        """To display the top item from the stack"""
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is EMPTY")
        
    def size(self):
        """To Display the Total items in the stack"""
        return self.item_count
    
    def insert_node_after_specific_node(self, val, data):
        """Overriding this function to restrict it into the stack"""
        try:
            if not self.is_empty():
                raise AttributeError("No 'insert_node_after_specific_node' function in Stack")
        except Exception as e:
            print(e)

    def insert_node_at_end(self, data):
        """Overriding this function to restrict it into the stack"""
        try:
            if not self.is_empty():
                raise AttributeError("No 'insert_node_at_end' function in Stack")
        except Exception as e:
            print(e)

    def delete_node_after_specific_node(self, val):
        """Overriding this function to restrict it into the stack"""
        try:
            if not self.is_empty():
                raise AttributeError("No 'delete_node_after_specific_node' function in Stack")
        except Exception as e:
            print(e)

    def delete_node_from_end(self):
        """Overriding this function to restrict it into the stack"""
        try:
            if not self.is_empty():
                raise AttributeError("No 'delete_node_from_end' function in Stack")
        except Exception as e:
            print(e)
    
st = Stack()
st.push(10)
st.push(20)
st.push(30) 
print("Size of Stack before pop operation::", st.size())
print("Top Value in the Stack ::", st.peek())
print("pop top value from the Stack ::", st.pop())
print("Size of Stack after pop operation::", st.size())
print("Top Value in the Stack ::", st.peek())
st.insert_node_after_specific_node(20, 40)
st.insert_node_at_end(50)
st.delete_node_after_specific_node(10)
st.delete_node_from_end()
print("Top Value in the Stack ::", st.peek())