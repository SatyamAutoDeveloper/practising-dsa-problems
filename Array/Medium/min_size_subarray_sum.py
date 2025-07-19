class MinSubArrayLen():
    def minSubArrayLen(self, target, nums):
        min_size = float('inf')
        left = 0 
        curr_sum = 0
        for right in range(len(nums)): 
            curr_sum += nums[right]
            while curr_sum >= target:
                min_size = min(min_size, right-left+1)
                curr_sum -= nums[left]
                left += 1
            
        return 0 if min_size == float('inf') else min_size
        

msal = MinSubArrayLen()
print("Min subarray length ::", msal.minSubArrayLen(4, [1,1,4]))

"""
The time complexity of the minSubArrayLen method is O(n), where n is the length of the input list nums. This is because each element is visited at most twice: once when the right pointer advances and once when the left pointer advances during the while loop. The for loop iterates through the list once, and the inner while loop moves the left pointer forward without re-examining previously processed elements, ensuring linear time complexity.

The space complexity is O(1) because the algorithm uses only a fixed amount of additional space, such as variables for min_size, left, curr_sum, and the loop counters. No extra data structures proportional to the input size are used, so the space complexity remains constant regardless of the input size.
"""