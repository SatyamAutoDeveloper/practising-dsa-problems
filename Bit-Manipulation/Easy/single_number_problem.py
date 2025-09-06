class Solution(object):
    def singleNumber(self, nums):
        uniqNum = 0
        for idx in nums:
            uniqNum ^= idx
        return uniqNum


sol = Solution()
print(sol.singleNumber([4, 1, 1, 2, 2]))


"""
Time Complexity:
- The method iterates through the list exactly once.
- Each iteration performs a constant-time XOR operation.
- Therefore, the overall time complexity is O(n), where n is the length of the input list.

Space Complexity:
- The algorithm uses only a few variables (`uniqNum` and `idx`), regardless of the input size.
- No additional data structures are used that grow with input size.
- Hence, the space complexity is O(1).

In summary, the solution runs in linear time and constant space.
"""


"""
Solution - 1   TC: O(n^2) and SC: O(1)

def singleNumber(self, nums):
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums.count(nums[left]) == 1:
            return nums[left]
        elif nums.count(nums[right]) == 1:
            return nums[right]
        left += 1
        right -= 1


Solution- 2  TC: O(n) and SC: O(n)

def singleNumber(self, nums):
    return 2 * sum(set(nums)) - sum(nums)

Solution- 3

def singleNumber(self, nums):
    return reduce(operator.xor, nums)
"""
