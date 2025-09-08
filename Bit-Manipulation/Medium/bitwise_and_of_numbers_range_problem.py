class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        count = 0
        while left != right:
            print(left, right)
            left >>= 1    # >> it removes the 1 bit from right of left binary.
            right >>= 1   # >> it removes the 1 bit from right of right binary.
            count += 1
        return left << count    # << it adds the number of 0's equal to count at the end of left bit. 
                                # e.g left is 1 and count is 2 then 100 is a binary of 4. 

sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))


"""
The time complexity of the rangeBitwiseAnd function is O(log n), where n is the difference between right and left (or more precisely, the maximum value between left and right). This is because in each iteration of the while loop, both left and right are right-shifted by one bit, effectively reducing their value by a factor of 2. The loop continues until left equals right, which takes at most the number of bits needed to represent the maximum of left and right. Since the number of bits in an integer is proportional to log n, the overall time complexity is O(log n).

The space complexity is O(1), as the algorithm uses only a fixed amount of additional space: a few integer variables (count, left, right) and no additional data structures that grow with input size. The operations performed are in-place bit shifts and comparisons, which do not require extra space proportional to input size.
"""