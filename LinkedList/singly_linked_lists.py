class NewNode:
    def __init__(self, item=None, next=None):
        """Construct the new node with 'None' value in item and next as default"""
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        """SLL is empty if start is none"""
        return self.start == None
    
    def insert_node_at_start(self, data):
        """To Insert a new node at start of SLL, add the new node reference in start node"""
        node = NewNode(data, self.start)
        self.start = node

    def insert_node_at_end(self, data):
        """To Insert a new node at last of SLL, Point the reference of new node to the next of last of existing SLL and enter None in the next of new node"""
        node = NewNode(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start=node

    def search_data(self, data):
        """To Search the Specific data, Run the while loop on complete SLL and stop it once you find your data else return None"""
        temp = self.start
        while temp is not None:
            if temp.item == data:
                print("Value Found in SLL:: ",temp.item)
                return temp
            temp = temp.next
        else:
            print("This Value is Not Found in SLL:: ",data)
            return None

    def insert_node_after_specific_node(self, val, data):
        """To Insert a new node after a specific node, search that specific node and then point the reference of new node to the next of specific node"""
        temp = self.search_data(val)
        if temp is not None:
            node = NewNode(data, temp.next)
            temp.next = node

    def traverse_and_count_node_in_sll(self):
        """To Traverse the complete SLL, Run While Loop till Node is not Null"""
        """To Count the Total Nodes in SLL, Use Counter with While Loop"""
        if not self.is_empty():
            temp = self.start
            count = 0
            while temp is not None:
                temp = temp.next
                count = count + 1
        print("Total Node in SLL ::", count)
        return count
    
    def delete_node_from_start(self):
        """ To Delete the 1st Node from SLL, Make 2nd Node as Start Node"""
        temp = self.start
        if temp is not None:
            self.start = self.start.next

    def delete_node_from_end(self):
        """To Delete the last node from SLL, Make next of 2nd last node is None"""
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                pre_temp = temp
                temp = temp.next
            pre_temp.next = None
            
        else:
            print("SLL is empty")
            return None
        
    def delete_node_after_specific_node(self, val):
        """To Delete a node after specific node, Point the reference of next node after delete node to the next of specific node"""
        temp = self.start
        #print("temp at line84 ::",temp.item)
        pre_temp = temp
        #print("pre_temp at line86 ::", pre_temp.item)
        while pre_temp.item != val:
            pre_temp = temp
            #print("pre_temp at line89 ::", pre_temp.item)
            temp = temp.next
            #print("temp at line91 ::", temp.item)
        pre_temp.next = temp.next

    def print_sll(self):
        """Print Data of SLL until None is found"""
        temp = self.start
        while temp is not None:
            print(temp.item, end="  ")
            temp = temp.next
 
sll = SinglyLinkedList()
sll.insert_node_at_start(2)
sll.insert_node_at_start(1)
sll.insert_node_at_end(10)
sll.insert_node_at_end(20)
sll.insert_node_after_specific_node(2, 5)
sll.insert_node_after_specific_node(5, 7)
sll.traverse_and_count_node_in_sll()
sll.delete_node_from_start()
sll.delete_node_from_end()
sll.delete_node_after_specific_node(7)
sll.print_sll()