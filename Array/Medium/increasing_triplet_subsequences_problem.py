class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        num_i = float("inf")
        num_j = float("inf")

        for num in nums:
            if num <= num_i:
                num_i = num
            elif num <= num_j:
                num_j = num
            else:
                return True
        return False


sol = Solution()
print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))

"""
The time complexity of the given code is O(n), where n is the length of the input list nums. This is because the algorithm iterates through the list exactly once, performing constant-time comparisons and updates during each iteration.

The space complexity is O(1), as the algorithm uses only a fixed number of variables (num_i and num_j) regardless of the size of the input list. No additional data structures proportional to the input size are used, so the space requirement remains constant.
"""

"""
Solution 1:: TC: O(n), SC: O(1)

def increasingTriplet(self, nums):
    if len(nums) < 3:
        return False

    num_i = float("inf")
    num_j = float("inf")

    for num in nums:
        if num_i < num_j < num:
            return True
        elif num < num_i:
            num_i = num
        elif num_i < num < num_j:
            num_j = num
    return False
"""
