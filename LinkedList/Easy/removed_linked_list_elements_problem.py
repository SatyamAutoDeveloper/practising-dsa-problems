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
Time Complexity:
- The initial while loop advances the head pointer past any nodes at the beginning with the target value. In the worst case, if multiple initial nodes have the target value, this loop runs in O(k), where k is the number of such nodes at the start.
- The second while loop traverses the remaining list once, checking each node's next node. Each node is visited at most once, so this loop runs in O(n - k), where n is the total number of nodes.
- Overall, since k ≤ n, the total time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for pointers (head, temp). No additional data structures are used that grow with input size.
- Therefore, the space complexity is O(1).
"""

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