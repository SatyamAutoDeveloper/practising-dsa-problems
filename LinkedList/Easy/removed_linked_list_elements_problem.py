class NewNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CreateLinkedList:
    def createLinkedList(self, values):
        if not values:
            return None
        head = NewNode(values[0])
        temp = head
        for value in values[1:]:
            temp.next = NewNode(value)
            temp = temp.next

        return head

class Solution(object):
    def removeElements(self, head, val):
        while head is not None and head.val == val:
            head = head.next

        temp = head
        while temp is not None and temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
    
cll = CreateLinkedList()
head = cll.createLinkedList([1,2,2,1])
sol = Solution()
sol.removeElements(head, 2)


"""
Solution 1: 

node = NewNode(0) 
node.next = head
temp = node
while temp is not None and temp.next is not None:
    if temp.next.val == val:
        temp.next = temp.next.next
    else:
        temp = temp.next
return node.next
"""