class NewNode:
    def __init__(self, prev=None, item=None, next=None):
        """Construct the new node with 'None' value in prev, item and next as default"""
        self.prev = prev
        self.item = item
        self.next = next

class CircularDoublyLinkedList:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_node_at_start(self, data):
        """To Insert the node at the start"""
        node = NewNode(item=data)
        if self.is_empty():
            node.next = node
            node.prev = node
        else:
            node.next = self.start
            node.prev = self.start.prev
            self.start.prev.next = node
            self.start.prev = node
        self.start = node

    def insert_node_at_last(self, data):
        node = NewNode(item=data)
        if self.is_empty():
            node.next = node
            node.prev = node
            self.start = node
        else:
            node.prev = self.start.prev
            node.next = self.start
            self.start.prev.next = node
            self.start.prev = node
            
    def search_data(self, val):
        """To search a specific node in CDLL"""
        temp = self.start
        if temp is not None:
            if temp.item == val:
                print("Value Found in CDLL::", temp.item)
                return temp
            temp = temp.next
            while temp is not self.start:
                if temp.item == val:
                    print("Value Found in CDLL ::", temp.item)
                    return temp
                temp = temp.next
            
            print("Value not found in CDLL", val)
            return None
        else:
            return None

    def insert_node_after_given_node(self, val, data):
        """To insert a node after given node"""
        temp = self.search_data(val)
        if temp is not None:
            node = NewNode(data)
            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node

    def traverse_backward_and_print_cdll(self):
        """To traverse backward and print items in cdll"""
        temp = self.start
        if not self.is_empty():
            temp = temp.prev
            while temp is not self.start:
                print("Data when moving backward in CDLL ::",temp.item)
                temp = temp.prev
            print("Data when moving backward in CDLL ::",temp.item)

    def delete_node_from_start(self):
        """To delete a node from start"""
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
        else:
            return None
        
    def delete_node_from_last(self):
        """To Delete Node from Last"""
        if not self.is_empty():
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_node_after_given_node(self, val):
        """To delete a node after given node"""
        temp = self.search_data(val)    
        if temp is not None:
            temp.next.next.prev = temp.next
            temp.next = temp.next.next
    
    def print_cdll(self):
        """To print the complete CDLL"""
        temp = self.start
        if temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end=" ")
                temp = temp.next
            print()

cll = CircularDoublyLinkedList()
cll.insert_node_at_start(2)
cll.insert_node_at_start(1)
cll.insert_node_at_last(10)
cll.insert_node_at_last(20)
cll.search_data(2)
cll.insert_node_after_given_node(2, 5)  #This Function is inserting 'None' after given value.(Need to debug it more)
cll.traverse_backward_and_print_cdll()
cll.delete_node_from_start()
cll.delete_node_from_last()
cll.delete_node_after_given_node(2)
cll.print_cdll()