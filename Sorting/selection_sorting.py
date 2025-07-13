class SelectionSort:
    def find_smallest_num(self, i, nums):
        smallest_num = 0
        for idx in range(i, len(nums)):
            if smallest_num == 0:
                smallest_num = nums[idx]
            elif nums[idx] < smallest_num:
                smallest_num = nums[idx]
        return smallest_num 

    def selectionSort(self, nums):
        """To sort the list using selection sort algorithm"""
        """It can be used for small data sets and it is 60% more efficient than bubble sort"""
        for i in range(0, len(nums)-1):
            num = self.find_smallest_num(i, nums)
            idx = nums.index(num)
            nums[i], nums[idx] = num, nums[i]
            print(nums)
        return nums
        

ss = SelectionSort()
print("Sorted List using selection sort is",ss.selectionSort([32,20,18,70,60,39,75,90,65]))