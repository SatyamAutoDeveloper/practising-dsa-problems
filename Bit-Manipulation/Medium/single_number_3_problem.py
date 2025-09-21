class Solution(object):
    def singleNumber(self, nums):
        uniqx = 0
        for num in nums:
            uniqx ^= num

        lowestbit = uniqx & -uniqx # -integer is called 2's complement or bitwise NOT of integer + 1
        "Calculation for -uniqx in 2s complement, In 1st complement all bits are flipped eg: for decimal 6, binary: 0110 "
        "using 1 compliment, binary will be: 1001 and then add 1 in 1001, so it becomes 1010 which is -6 in decimal"

        result = [0, 0]
        for num in nums:
            if lowestbit & num == 0:
                result[0] ^= num
            else:
                result[1] ^= num

        return result


sol = Solution()
print(sol.singleNumber([1, 2, 1, 3, 2, 5]))


"""
Time Complexity: O(n) Space Complexity: O(1)
"""

"""
Solution 1:: TC: O(n) SC: O(n)

def singleNumber(self, nums):
    occurences_dict1 = {}
        
    #get the number of occurences of each num 
    for num in nums:
        occurences_dict1[num] = occurences_dict1.get(num, 0) + 1
        
    #get both the num with count equals to 1
    result = [num for num, count in occurences_dict1.items() if count == 1]
    return result
"""
