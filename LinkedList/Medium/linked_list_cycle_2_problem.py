class NewNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class CreateLinkedList:
    def create_linked_list(self, values):
        if not values:
            return None
        head = NewNode(values[0])
        temp = head
        for value in values[1:]:
            temp.next = NewNode(value)
            temp = temp.next
        return head

class DetectCycle():
    def detectCycle(self, head):
        if not head:
            return None
        try:
            slow = head
            fast = head.next
            while slow != fast:
                if not fast:
                    return None
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        
        slow = slow.next
        while head != slow:
            head = head.next
            slow = slow.next
        return head

cll = CreateLinkedList()
dc = DetectCycle()
head = cll.create_linked_list([3,2,0,-4])
dc.detectCycle(head)


"""
Time Complexity:
- Creating the linked list from a list of n values takes O(n) time because it iterates through all elements once.
- Detecting a cycle involves traversing nodes with two pointers (slow and fast). In the worst case, the cycle detection traverses all nodes until the cycle is found or the end is reached, which is also O(n).
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The creation of the linked list uses O(n) space to store n nodes.
- The cycle detection algorithm uses only a fixed number of pointers (slow, fast, head, and temp), so it uses O(1) additional space.
- Overall, the space complexity is O(n) due to the linked list storage, with constant extra space for detection.

In summary:
Time complexity: O(n)
Space complexity: O(n)
"""