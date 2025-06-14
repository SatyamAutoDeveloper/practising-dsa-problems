class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    
    def push(self, data):
        """To Push the data at the last of stack"""
        self.item.append(data)

    def pop(self):
        """To pop the last item from the stack"""
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is EMPTY")

    def peek(self):
        """To display the last item in the stack without popping the item"""
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is EMPTY")
        
    def size(self):
        """To get the size of stack"""
        return len(self.item)

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