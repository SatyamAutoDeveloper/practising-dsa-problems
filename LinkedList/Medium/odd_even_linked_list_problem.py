
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
    def oddEvenList(self, head):
        if head is None:
            return None

        odd = head #odd pointer
        even = odd.next  #odd.next point to -> even
        even_head = even #we have to connect the last odd node to first even node
        while even and even.next is not None:
            odd.next = even.next #1->3
            odd = odd.next #odd = 3
            even.next = odd.next #2->4
            even = even.next #even = 4
        odd.next = even_head #we have to connect the last odd node to first even node (even_head)

        return head
            
        
cll = CreateLinkedList()
head = cll.create_linked_list([1,2,3,4,5])
sol = Solution()
print(sol.oddEvenList(head))


"""
The time complexity of this solution is O(n), where n is the number of nodes in the linked list. This is because the algorithm traverses the list once, processing each node exactly one time during the while loop.

The space complexity is O(1), as the algorithm only uses a fixed number of pointers (odd, even, even_head) regardless of the size of the input list. It rearranges the existing nodes without allocating additional data structures proportional to the input size.
"""