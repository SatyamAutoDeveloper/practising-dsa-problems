class QuickSort:
    def quickSortProcess(self, nums, l, r):
        left = l
        right = r
        loc = l

        while loc != right:
            if nums[loc] > nums[right]:
                nums[loc], nums[right] = nums[right], nums[loc]
                loc = right
            else:
                right -= 1
        
        while loc != left:
            if nums[loc] < nums[left]:
                nums[loc], nums[left] = nums[left], nums[loc]
                loc = left
            else:
                left += 1

        return loc
    
    def quickSortHelper(self, nums, left, right):
        if left < right:
            loc = self.quickSortProcess(nums, left, right)
            self.quickSortHelper(nums, left, loc)
            self.quickSortHelper(nums, loc+1, right)

    def quickSort(self, nums):
        """To sort the list using quick sort algorithm"""
        left = 0
        right = len(nums)-1
        self.quickSortHelper(nums, left, right)
        return nums

qs = QuickSort()
print("Sorted List using Quick Sort:: ", qs.quickSort([32,20,18,70,60,39,75,90,65]))