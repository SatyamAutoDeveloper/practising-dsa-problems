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