class RemoveDuplicates:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]
        return i + 1

rd = RemoveDuplicates()
k = rd.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) 
print("K ::", k) #k=5, unique list = [0,1,2,3,4]