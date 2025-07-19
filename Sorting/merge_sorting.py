class MergeSort:
    def mergeProcess(self, nums, lefthalf, righthalf):
        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nums[k] = lefthalf[i]
                i += 1
            else:
                nums[k] = righthalf[j]
                j += 1
            k +=1
        
        while i < len(lefthalf):
            nums[k] = lefthalf[i]
            k += 1
            i += 1
        while j < len(righthalf):
            nums[k] = righthalf[j]
            k += 1
            j += 1

    def mergeSort(self, nums):
        """To sort the list using merge sort"""
        left = 0
        right = len(nums)
        if len(nums) > 1:
            mid = left + right // 2
            lefthalf = nums[:mid]
            righthalf = nums[mid:]
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)
            self.mergeProcess(nums, lefthalf, righthalf)
        return nums

ms = MergeSort()
print("Sorted List using Merge Sort ::", ms.mergeSort([32,20,18,70,60,39,75,90,65]))