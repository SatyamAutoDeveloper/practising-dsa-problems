"""Time Complexity: O(N^2)"""
"""Space Complexity: O(1)"""

class MoveZeroes:
    def moveZeroes(self, nums):
        if len(nums) == 1:
            print("return nums")
        else:
            left = 0 
            right = len(nums)-1
            while left < right:
                if nums[left] == 0:
                    nums.append(nums[left])
                    nums.pop(left)
                    right -=1
                else:
                    left +=1
        print(nums)

mz = MoveZeroes()
mz.moveZeroes([1,2,0,0,4,0,0,0,12,0])


"""
Solution 2: TC: O(n) and SC: O(1)

def moveZeroes(self, nums):
	zero = 0  # records the position of "0"
	for i in range(len(nums)):  
	    if nums[i] != 0:
			nums[i], nums[zero] = nums[zero], nums[i]
			zero += 1	    
	return nums
"""