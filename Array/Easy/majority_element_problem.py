
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