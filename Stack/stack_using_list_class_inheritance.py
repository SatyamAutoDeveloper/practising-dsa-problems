class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        """To Push the data into the stack"""
        self.append(data)

    def pop(self):
        """To pop the last item from the stack"""
        if not self.is_empty():
            return super().pop()    #Super() is indicating parent class i.e List Class.
        else:
            raise IndexError("Stack is EMPTY")
    
    def peek(self):
        """To display the top item from the stack"""
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is EMPTY")
    
    def size(self):
        """To get the size of the stack"""
        return len(self)
    
    def insert(self, index, data):
        """To disable the list insert function"""
        try: 
           raise AttributeError("No 'insert' Operation in Stack")
        except Exception as e:
            print(e)
    
st = Stack()
st.push(10)
st.push(20)
st.push(30)
stack_size = st.size()
print("Stack Size before pop operation ::", stack_size)
before_top_val = st.peek()
print("Top Item in stack before pop operation ::", before_top_val)
pop_top_val = st.pop()
print("Top Item Popped from stack ::", pop_top_val)
after_top_val = st.peek()
print("Top Item in stack after pop operation ::", after_top_val)
stack_size = st.size()
print("Stack Size after pop operation ::", stack_size)
st.insert(5, 50)
st.push(40)
top_val = st.peek()
print("Top Item in stack ::", top_val)