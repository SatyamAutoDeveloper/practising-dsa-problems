"""
Time complexity: O(n)
Space complexity: O(n)
"""

class ContainsDuplicate2:
    def containsDuplicate2(self, nums, k):
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1 and abs(i-dict1[nums[i]]) <= k:
                return True
            dict1[nums[i]] = i
        return False

cd2 = ContainsDuplicate2()
print("Duplicates distinct indices substraction is equal to or less than K ::",cd2.containsDuplicate2([1,0,1,1], 1))