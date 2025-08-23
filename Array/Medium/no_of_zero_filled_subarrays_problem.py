class Solution(object):
    def zeroFilledSubarray(self, nums):
        total_subarray_zeros = 0
        current_subarray_zeros = 0

        for num in nums:
            if num == 0:
                current_subarray_zeros += 1
                total_subarray_zeros += current_subarray_zeros
            else:
                current_subarray_zeros = 0

        return total_subarray_zeros


sol = Solution()
print(sol.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))

"""
The time complexity of the given code is O(n), where n is the length of the input list nums. This is because the code iterates through the list exactly once, performing constant-time operations during each iteration.

The space complexity is O(1), as the algorithm uses only a fixed amount of additional space regardless of the input size. It maintains a few integer variables (total_subarray_zeros and current_subarray_zeros) without utilizing any extra data structures that grow with input size.
"""
