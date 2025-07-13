class BubbleSort:
    def bubble_sort(self, nums):
        """To sort the array using bubble sort algo"""
        """Time Complexity: O(n^2)"""
        for i in range(0, len(nums)-1):
            left = 0
            right = 1
            while right != len(nums)-i:
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            
        return nums
    
    def optimized_bubble_sort(self, nums):
        """To sort the array using optimized bubble sort algo"""
        """It will not run the remaining passes once no swapping required/List is sorted"""

        self.is_sorted = False
        for i in range(0, len(nums)-1):
            left = 0
            right = 1
            while right != len(nums)-i:
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    self.is_sorted = False
                else:
                    self.is_sorted = True
                left += 1
                right += 1
            if self.is_sorted is True:
                return nums
        

bs = BubbleSort()
print("Sorted List using bubble sort is",bs.bubble_sort([12,20,18,70,60,39,75,90,85]))
print("Sorted List using optimized bubble sort is",bs.optimized_bubble_sort([12,20,18,70,60,39,75,90,65]))