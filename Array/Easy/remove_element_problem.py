class RemoveElement:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

re = RemoveElement()
print("K element in nums ::", re.removeElement([3,2,2,3], 3))

"""
The provided code defines a method to remove all instances of a specified value (val) from a list (nums) in-place and returns the new length (k) of the modified list.

Time Complexity:
- The method iterates through the entire list exactly once, with a for loop that runs from 0 to len(nums) - 1.
- Each iteration performs a constant amount of work (comparison and possibly assignment).
- Therefore, the overall time complexity is O(n), where n is the length of the input list.

Space Complexity:
- The algorithm modifies the input list in-place and uses only a few additional variables (k and i).
- No extra space proportional to the input size is allocated.
- Hence, the space complexity is O(1).

In summary:
Time complexity: O(n)
Space complexity: O(1)
"""