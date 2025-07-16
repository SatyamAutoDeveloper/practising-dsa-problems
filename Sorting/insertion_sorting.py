class InsertionSort:
    def insertionSort(self, nums):
        """To sort the list using insertion sort algorithm"""
        for i in range(1, len(nums)):
            temp = nums[i]
            for idx in range(i, 0, -1):
                if temp > nums[idx-1]:
                    break
                elif temp < nums[idx-1]:
                    nums[idx-1], nums[idx] = temp, nums[idx-1]

        return nums
        
s = InsertionSort()
print("Sorted List using insertion sort ::",s.insertionSort([32,20,18,70,60,39,75,90,65]))