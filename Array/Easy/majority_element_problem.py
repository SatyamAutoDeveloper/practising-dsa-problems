
class Solution(object):
    def majorityElement(self, nums):
        curr, count = nums[0], 1   
        for num in nums[1:]:
            if curr == num:
                count += 1
            else: 
                count -= 1 				
            if not count:       
                curr = num
                count = 1
        return curr		
	
sol = Solution()
print(sol.majorityElement([3,2,3])) 


"""
The provided code implements the Boyer-Moore Majority Vote algorithm to find the majority element in a list.

Time Complexity:
- The algorithm iterates through the list exactly once, processing each element in constant time.
- Therefore, the overall time complexity is O(n), where n is the length of the list.

Space Complexity:
- The algorithm uses only a fixed number of variables (curr and count), regardless of the input size.
- Hence, the space complexity is O(1).

In summary:
Time complexity is linear, O(n), and space complexity is constant, O(1).
"""

"""
Solution 1:: TC: O(n), SC: O(n)

def majorityElement(self, nums):
    majority_count = {}
    for num in nums:
        if num in majority_count:
            majority_count[num] += 1
        else:
            majority_count[num] = 1
    for k,v in majority_count.items():
        if v == max(majority_count.values()):
            return k
"""

"""
Solution 2:: TC: O(nlogn), SC: O(n)

def majorityElement(self, nums):
    nums.sort()
    return nums[len(nums)// 2]
"""