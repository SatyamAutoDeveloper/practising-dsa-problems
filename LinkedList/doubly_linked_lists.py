class NewNode:
    def __init__(self, prev=None, item=None, next=None):
        """Construct the new node with 'None' value in prev, item and next as default"""
        self.prev = prev
        self.item = item
        self.next = next


class DoublyLinkedList:
    def __init__(self, start=None):
        """Initialize the start"""
        self.start = start

    def is_empty(self):
        """DLL is empty if start is none"""
        return self.start == None
    
    def insert_node_at_start(self, data):
        """To Insert a new node at start of DLL"""
        node = NewNode(None, data, self.start)
        if not self.is_empty():
            self.start.prev = node
        self.start = node

    def insert_node_at_end(self, data):
        """To Insert a new node at end of DLL"""
        node = NewNode("", data, None)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp
        else:
            self.start.prev = node

    def search_data(self, data):
        """To Search the specific data in the DLL"""
        temp = self.start 
        while temp is not None:
            if temp.item == data:
                print("Data Found in DLL ::", temp.item) 
                return temp  
            temp = temp.next

        else:
            print("Data is not found in DLL")
            return None
            
    def insert_node_after_given_node(self, specific_node, data):
        """To Insert node after the specific node in the DLL"""
        temp = self.search_data(specific_node)
        if temp is not None:
            node = NewNode(temp, data, temp.next)
            node.next = temp.next
            node.prev = temp
            temp.next = node
            temp.next.prev = node
        else:
            node = NewNode("", data, None)
            self.start = node
            node.prev = self.start

    def traverse_forward_and_count_node_in_dll(self):
        """To Traverse Forward in DLL and Count Total Nodes"""
        temp = self.start
        if not self.is_empty():
            count = 0
            while temp is not None:
                count = count + 1
                temp = temp.next
            print("Total Node in DLL::", count)
        else:
            return None
        
    def traverse_backward_and_print_data_of_nodes_in_dll(self, val):
        """To Traverse Backward in DLL and Print Each Node Data"""
        temp = self.search_data(val)
        if not self.is_empty():
            while temp != self.start.prev:
                print("Data when moving backward in DLL ::", temp.item)
                temp = temp.prev
        else:
            return None
        
    def delete_node_from_start(self):
        """To Delete Node from Start in DLL"""
        if not self.is_empty():
            temp = self.start
            self.start = temp.next
            temp.prev = None
        else:
            return None

    def delete_node_from_last(self):
        """To Delete Node from Last in DLL"""   
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None           
        else:
            return None
        
    def delete_node_after_given_node(self, val):
        """To delete node after a specific node"""
        temp = self.search_data(val)
        temp.next = temp.next.next

    def print_dll(self):
        "To Print the Complete DLL"
        temp = self.start 
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

dll = DoublyLinkedList()
dll.insert_node_at_start(2)
dll.insert_node_at_start(1)
dll.insert_node_at_end(10)
dll.insert_node_at_end(20)
#dll.search_data(10)
#dll.insert_node_after_given_node(2, 7)
dll.insert_node_after_given_node(2, 5)
dll.traverse_forward_and_count_node_in_dll()
dll.traverse_backward_and_print_data_of_nodes_in_dll(20)
#dll.delete_node_from_start()
#dll.delete_node_from_last()
#dll.delete_node_after_given_node(2)
dll.print_dll()