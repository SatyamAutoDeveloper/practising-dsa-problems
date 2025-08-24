class Solution(object):
    def firstMissingPositive(self, nums):
        set_nums = set(nums)
        i = 1
        while i in set_nums:
            i += 1
        return i


sol = Solution()
print(sol.firstMissingPositive([2, 1]))


"""
The provided code for the firstMissingPositive function uses a set to track elements and then iterates through integers starting from 1 upwards until it finds a missing positive integer. 

Time complexity: O(n). Creating the set takes O(n) time. The while loop, in the worst case, can iterate up to n+1 times (if the missing positive is just beyond the maximum element). Checking membership in a set is O(1), so overall, the process remains linear with respect to the size of the input array.

Space complexity: O(n). The set created from the input array requires additional space proportional to the size of the input, as it stores all elements in a separate data structure. No other significant extra space is used, so the total space complexity is linear.
"""


"""
The time complexity of the given code is O(n). This is because each element in the array is swapped at most once or twice, and the inner while loop ensures that each element is moved to its correct position without unnecessary repetitions. The outer for loop runs n times, and the inner while loop, across all iterations, collectively performs at most n swaps, leading to an overall linear time complexity.

The space complexity is O(1), meaning it uses constant extra space. The algorithm modifies the input array in place and only uses a few additional variables (like n and idx), which do not depend on the size of the input array. Therefore, the space used remains constant regardless of the input size.

Solution 1::

def firstMissingPositive(self, nums):
    def swap_and_position_num_in_sequence(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(nums)
    for idx in range(n):
        while 0 < nums[idx] <= n and nums[idx] != nums[nums[idx] - 1]:
            swap_and_position_num_in_sequence(nums, idx, nums[idx] - 1)

    for idx in range(n):
        if nums[idx] != idx + 1:
            return idx + 1

    return n + 1

"""
