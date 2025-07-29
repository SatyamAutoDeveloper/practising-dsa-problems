class BinarySearch:
    def binarySearchHelper(self, nums, value, left, right):
        """To help in searching the item in nums using binary search technique"""
    
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == value:
                return mid
            elif nums[mid] > value:
                right = mid - 1
            else:
                left = mid + 1
        return None
    

    def binarySearch(self, nums, value):
        """To search the item in nums using binary search technique"""
        if not nums:
            return None
        nums = sorted(nums)
        left = 0
        right = len(nums)
        return self.binarySearchHelper(nums, value, left, right)
        

bs = BinarySearch()
print("value at index in nums :: ", bs.binarySearch([12,20,18,70,60,39,75,90,85], 17))