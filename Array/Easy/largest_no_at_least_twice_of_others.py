"""This problem is asking us to find the index of largest number in the array
 where largest number will be at least double of other values in the array"""

class LargestNumberTwiceOfOthers:
    def largest_number_twice_of_others(self, nums):
        self.nums = nums
        sorted_arr = sorted(self.nums)
        largest_num = sorted_arr[-1]
        
        for i in range(len(sorted_arr)):
            if sorted_arr[i] == 0 or largest_num == sorted_arr[i]:
                pass
            elif (largest_num // sorted_arr[i]) >= 2:
                continue
            else:
                return -1
        return self.nums.index(largest_num)

largenumber = LargestNumberTwiceOfOthers()
largest_val_index = largenumber.largest_number_twice_of_others([1,2,3,4])
print("Index of Largest Number which twice of others or No such Number::", largest_val_index)
