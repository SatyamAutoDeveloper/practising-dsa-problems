
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CreateLinkedList:
    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        temp = head
        for val in values[1:]:
            temp.next = ListNode(val)
            temp = temp.next
        return head 

class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = ListNode(0, head)
        left = temp
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return temp.next


sol = Solution()
cll = CreateLinkedList()
head = cll.create_linked_list([1,2])
print(sol.removeNthFromEnd(head, 1))

"""
Time Complexity:
- The algorithm traverses the list with the right pointer until it reaches the end, which takes O(L) time, where L is the length of the list.
- The initial traversal to move the right pointer n steps forward is O(n), which is at most O(L).
- The second traversal moves both pointers until the right pointer reaches the end, which again is O(L - n).
- Overall, the total time complexity is O(L), since the list is traversed at most twice, but these traversals are sequential, not nested.

Space Complexity:
- The algorithm uses a constant amount of extra space for pointers (temp, left, right), regardless of the size of the input list.
- No additional data structures proportional to the input size are used.

In summary:
Time complexity is O(L), where L is the length of the list.
Space complexity is O(1).
"""