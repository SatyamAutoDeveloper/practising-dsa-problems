class FindMaxConsecutiveOnes():
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_ones = max(max_ones, count)
                print(max_ones, count)
            else:
                count = 0
        
        return max_ones

fmco = FindMaxConsecutiveOnes()
print("Max Consecutive Ones is ::",fmco.findMaxConsecutiveOnes([1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

"""
The time complexity of this solution is O(n), where n is the length of the input list nums. This is because the algorithm iterates through the list exactly once, performing constant-time operations for each element.

The space complexity is O(1), as the algorithm uses only a fixed amount of extra space (variables max_ones and count), regardless of the size of the input list.

In summary:
- Time complexity: O(n)
- Space complexity: O(1)
"""