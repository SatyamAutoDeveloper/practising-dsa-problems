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
    def isPalindrome(self, head):
        slow = head
        fast = head
        # find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        #reverse the 2nd half.
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        fast = head
        slow = prev
        #compare the values
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True
        

cll = CreateLinkedList()
head = cll.create_linked_list([1,2])
sol = Solution()
print(sol.isPalindrome(head))


"""
The time complexity of this solution is O(n), where n is the number of nodes in the linked list. This is because the algorithm traverses the list multiple times: once to find the middle node, once to reverse the second half, and once to compare the two halves. Each of these steps is linear in the size of the list, so overall, the process is linear.

The space complexity is O(1), as the algorithm only uses a fixed number of pointers (slow, fast, prev, next_node, etc.) regardless of the size of the input list. It modifies the list in place for the reversal step and does not allocate additional data structures proportional to the input size.
"""


"""
Solution 1:

def isPalindrome(self, head):
    if head is None:
        return True
    temp = head
    list1 = []
    while temp is not None:
        list1.append(temp.val)
        temp = temp.next
    print(list1)
    if list1 == list1[::-1]:
        return True
    else:
        return False
"""