class MergeSort:

    def divide_and_conqure(self, nums):
        left = 0
        right = len(nums)
        mid = left + right // 2
        rightArridx = mid + 1
        conqure_list = []
        
        while left <= mid:
            if nums[left] < nums[rightArridx]:
                conqure_list.append(nums[left])
                left += 1
            else:
                conqure_list.append(nums[rightArridx])
                rightArridx += 1
        return conqure_list

    def mergeSort(self, nums):
        """To sort the list using merge sort"""
        left = 0
        right = len(nums)
        mid = self.divide(nums)
        sorted_list = self.conqure(mid, nums[left:mid+1], nums[mid+1, right])
        print("sorted list", sorted_list)

ms = MergeSort()
print("Sorted List using Merge Sort ::", ms.divide_and_conqure([32,20,18,70,60,39,75,90,65]))