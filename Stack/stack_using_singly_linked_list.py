class NewNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self, data):
        """To Push the data at the last of stack"""
        node = NewNode(data)
        if not self.is_empty():
            node.next = self.start
        self.start = node
        self.item_count += 1

    def pop(self):
        """To pop the last item from the stack"""
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
        else:
            raise IndexError("Stack is EMPTY")
        return data

    def peek(self):
        """To display the last item in the stack without popping the item"""
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is EMPTY")
        
    def size(self):
        """To get the size of stack"""
        return self.item_count 

st = Stack()
st.push(10)
st.push(20)
st.push(30)
top_val = st.peek()
st_size = st.size()
print("Size of Stack before pop operation::", st_size)
print("Top Value in the Stack ::",top_val)
top_val = st.pop()
print("pop top value from the Stack ::",top_val)
top_val = st.peek()
st_size = st.size()
print("Size of Stack after pop operation::", st_size)
print("Top Value in the Stack ::",top_val)