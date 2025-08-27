class NewNode:
    def __init__(self, prev=None, val=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next


class MyLinkedList:

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
                if self.count != 0:
                    self.head.prev = node
                self.head = node
            else:
                temp = self.head
                for _ in range(index - 1):
                    temp = temp.next
                if temp:
                    node.next = temp.next
                    node.prev = temp
                    temp.next = node
                    temp.next.prev = node
                else:
                    node.prev = temp
                    node.next = None
                temp.next = node

            self.count += 1

    def deleteAtIndex(self, index):
        if self.count > index:
            if index == 0:
                temp = self.head
                self.head = temp.next
                temp.prev = None
            else:
                temp = self.head
                for _ in range(index - 1):
                    temp = temp.next
                temp.next = temp.next.next
            self.count -= 1


obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(1)
obj.get(1)


"""
The provided code implements a doubly linked list with methods for getting, adding, and deleting nodes at specific indices.

Time Complexity:
- get(index): O(index) in the worst case, since it traverses from the head to the specified index.
- addAtHead(val): O(1), as it inserts at the beginning.
- addAtTail(val): O(count), because it traverses to the end of the list to insert.
- addAtIndex(index, val): O(index), as it traverses to the node before the insertion point.
- deleteAtIndex(index): O(index), since it traverses to the node to delete.

Space Complexity:
- O(n), where n is the number of nodes in the list, due to storing each node with prev, val, and next pointers. The auxiliary space used by the methods themselves is constant, but the overall space depends on the number of nodes stored.
"""
