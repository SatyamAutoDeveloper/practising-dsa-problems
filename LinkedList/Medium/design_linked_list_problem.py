class NewNode():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList():

    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get(self, index):
        if self.count > index:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next 
            return temp.val
        return -1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index, val):
        node = NewNode(val)
        if 0 <= index <= self.count:
            if index == 0:
                node.next = self.head
                self.head = node
            else:
                temp = self.head
                for _ in range(index-1):
                    temp = temp.next
                if temp:
                    node.next = temp.next
                else:
                    node.next = None
                temp.next = node
            self.count += 1


    def deleteAtIndex(self, index): 
        if self.count > index:
            if index == 0:
                self.head = self.head.next
            else:
                temp = self.head
                for _ in range(index-1):
                    temp = temp.next
                temp.next = temp.next.next
            self.count -= 1
        
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))

"""
Time Complexity:
- get(index): O(index) in the worst case, because it traverses from the head to the specified index.
- addAtHead(val): O(1), as it inserts at the beginning.
- addAtTail(val): O(n), since it calls addAtIndex at position count, which requires traversing the entire list.
- addAtIndex(index, val): O(index), because it traverses up to the position before the insertion point.
- deleteAtIndex(index): O(index), as it traverses to the node just before the target index for deletion.

Space Complexity:
- O(n), where n is the number of nodes in the linked list, due to storing each node separately.
- Additional space is used for temporary variables during traversal, which is constant.
"""