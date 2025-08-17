class Solution(object):
	def productExceptSelf(self, nums):
		n = len(nums)
		answer = [1] * n

		prefix = 1
		for i in range(n):
			answer[i] = prefix
			prefix *= nums[i]

		suffix = 1
		for i in range(n-1, -1, -1):
			answer[i] *= suffix
			suffix *= nums[i]

		return answer

sol = Solution()
print(sol.productExceptSelf([-1,1,0,-3,3]))


"""
The time complexity of the provided code is O(n), where n is the length of the input list nums. This is because the algorithm performs two separate passes over the list: one forward pass to compute prefix products and one backward pass to incorporate suffix products. Each pass iterates through the list once, resulting in linear time complexity.

The space complexity is O(1) additional space, aside from the output list. The answer list is used to store the final result and is not counted as extra space since it is required for the output. The variables prefix and suffix are used for intermediate calculations and occupy constant space. Therefore, the overall auxiliary space complexity is O(1).
"""


"""
Solution 1:: TC: O(n^2) SC: O(n)

new_nums = [1]*len(nums)
for i in range(len(nums)):
	for j in range(len(nums)):
		if i != j:
			new_nums[i] *= nums[j]
return new_nums	
"""