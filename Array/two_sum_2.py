
class TwoSum2():
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while left < right:
            num =  numbers[left] + numbers[right]
            if num == target:
                return [left+1, right+1]
            elif num < target:
                left += 1
            else:
                right -= 1    

ts2 = TwoSum2()
print("List of indices ::", ts2.twoSum([1,2,3,4,6,15], 6))

"""
The provided code implements a two-pointer approach to find two numbers in a sorted list that sum up to a target value.

Time Complexity:
- The algorithm uses a while loop that advances either the left or right pointer in each iteration.
- Since each pointer moves at most the length of the list once, the total number of iterations is proportional to the size of the list.
- Therefore, the time complexity is O(n), where n is the length of the input list.

Space Complexity:
- The algorithm uses only a fixed number of variables (left, right, num), regardless of input size.
- It does not allocate additional space proportional to the input size.
- Hence, the space complexity is O(1).

In summary:
- Time Complexity: O(n)
- Space Complexity: O(1)
"""