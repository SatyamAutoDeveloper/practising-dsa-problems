"""Pivot Index is a index where sum of values on its left is equal to sum of values on its right"""
class Solution:
    def pivotIndex(self, nums):
        self.nums = nums
        prefixSum = []
        for i in range(len(self.nums)):
            if i == 0 :
               prefixSum.append(self.nums[i])
            elif i > 0: 
                prefixSum.append(prefixSum[i-1] + self.nums[i])
            
        print("prefixSum list:: ", prefixSum) 
        total = sum(self.nums)
        for i in range(len(self.nums)):
            sumRight = total - prefixSum[i]    
            sumLeft = prefixSum[i] - self.nums[i]
            if sumLeft == sumRight:
                return i
        else:
            return -1
            
        
sol = Solution()
pivotindexval = sol.pivotIndex([1,12,11,1,4,20])
print("pivot index:: ", pivotindexval)