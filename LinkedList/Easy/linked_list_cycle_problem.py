class NewNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CreateLinkedList:
    def create_linked_list_from_input(self, values):
        if not values:
            return None
        head = NewNode(values[0])
        temp = head
        for val in values[1:]:
            temp.next = NewNode(val)
            temp = temp.next
        return head    

class LinkedListCycle():
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

cll = CreateLinkedList()
head = cll.create_linked_list_from_input([3,2,0,-4])
llc = LinkedListCycle()
llc.hasCycle(head)

"""
The time complexity of the hasCycle method is O(n), where n is the number of nodes in the linked list. This is because, in the worst case, the slow and fast pointers traverse the list once until they either meet (detecting a cycle) or reach the end (no cycle). The fast pointer moves twice as fast as the slow pointer, but overall, each node is visited at most a constant number of times.

The space complexity is O(1), as the algorithm only uses a fixed amount of extra space for the two pointers (slow and fast), regardless of the size of the linked list. No additional data structures proportional to the input size are used.
"""