class NewNode:
    def __init__(self, item=None, next=None):
        """Construct the new node with 'None' value in item and next as default"""
        self.item = item
        self.next = next

class CircularSinglyLinkedList:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last == None
    
    def insert_node_at_start(self, data):
        """To Insert the node at start"""
        node = NewNode(data)
        if self.is_empty(): 
            node.next = node
            self.last = node
        else:
            node.next = self.last.next
            self.last.next = node

    def insert_node_at_last(self, data):
        """To insert the node at last"""
        node = NewNode(data)
        if self.is_empty():
            node.next = node
            self.last = node
        else:
            self.last.next = node
            node.next = self.last.next
            self.last = node

    def search_data(self, val):
        temp = self.last.next
        while temp != self.last:
            if temp.item == val:
                print("Value Found in CSLL ::", temp.item)
                return temp
            temp = temp.next
        else:
            if temp.item == val:
                print("Value Found is a last node in CSLL ::", temp.item)
                return temp
            else:
                print("Value Not Found in CSLL ::", val)
                return None
        
    def insert_after_given_node(self, val, data):
        """To Insert a node after a given node"""
        temp = self.search_data(val)
        node = NewNode(data)
        if temp != self.last:
            node.next = temp.next
            temp.next = node
        else:
            node.next = temp.next
            temp.next = node
            self.last = node

    def delete_node_from_start(self):
        """To Delete Node from Start"""
        if not self.is_empty():
            temp = self.last.next
            self.last.next = temp.next
        else:
            self.last = None
        
    def delete_node_from_last(self):
        """To Delete Node from Last"""
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_node_after_given_node(self, val):
        """To Delete Node after a given node"""
        if not self.is_empty():
            temp = self.search_data(val)
            if temp.next == self.last:
                temp.next = self.last.next
                self.last = temp
            else:
                temp.next = temp.next.next
        

    def print_csll(self):
        """To print the complete CSLL"""
        if self.is_empty():
            print(self.last.item, " ")
        else:
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item, end=" ")

cll = CircularSinglyLinkedList()
cll.insert_node_at_last(10)
cll.insert_node_at_start(2)
cll.insert_node_at_start(1)
cll.search_data(10)
cll.insert_after_given_node(2,5)
cll.delete_node_from_start()
cll.delete_node_from_last()
cll.delete_node_after_given_node(2)
cll.print_csll()