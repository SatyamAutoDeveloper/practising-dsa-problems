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
        for val in values[1:]:
            temp.next = NewNode(val)
            temp = temp.next
        return head 
    

class Solution():
    def getIntersectionNode(self, headA, headB):
        A = headA
        B = headB

        unique_set = set()
        while A is not None:
            unique_set.add(A)
            A = A.next

        while B is not None:
            if B in unique_set:
                return B
            B = B.next

        return None
        

cll = CreateLinkedList()
sol = Solution()
headA = cll.create_linked_list([4,1,8,4,5])
headB = cll.create_linked_list([5,6,1,8,4,5])
print(sol.getIntersectionNode(headA, headB))


"""
Time Complexity:
- The first while loop traverses list A entirely, which takes O(m) time, where m is the length of list A.
- The second while loop traverses list B, which takes O(n) time, where n is the length of list B.
- Checking membership in a set is an average O(1) operation.
- Overall, the total time complexity is O(m + n).

Space Complexity:
- The set stores references to nodes from list A, which in the worst case could be all nodes in list A.
- Therefore, the space complexity is O(m).

In summary:
- Time complexity: O(m + n)
- Space complexity: O(m)
"""

"""
Solution 1:

def getIntersectionNode(self, headA, headB):
    A = headA
    B = headB
        
    while A is not B:
        if A is None:
            A = headB
        else:
            A = A.next
                
        if B is None:
            B = headA
        else:
            B = B.next
    return A
"""