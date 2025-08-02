class NewNode:
    def __init__(self, val=None, next=None):
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
    def reverseList(self, head):
        prev = None
        temp = head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next   
        return prev

sol = Solution()
cll = CreateLinkedList()
head = cll.createLinkedList([1,2,3,4,5])
print(sol.reverseList(head))

"""
Time Complexity:
- The algorithm traverses each node exactly once.
- For each node, it performs a constant number of operations (reassigning pointers).
- Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses only a fixed number of additional variables (`prev`, `temp`, `next`).
- No extra space proportional to the size of the input list is allocated.
- Hence, the space complexity is O(1).

In summary:
Time complexity: O(n)
Space complexity: O(1)
"""