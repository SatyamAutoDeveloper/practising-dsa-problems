class Solution(object):
    def hammingWeight(self, n):
        hammingWeight = 0
        while n > 0:
            carry = n % 2
            if carry > 0:
                hammingWeight += 1
            n = n // 2

        return hammingWeight


sol = Solution()
print(sol.hammingWeight(11))


"""
The provided code calculates the number of '1' bits (Hamming weight) in the binary representation of an integer n.

Time Complexity:
- The while loop runs as long as n > 0.
- In each iteration, n is divided by 2 (integer division), effectively shifting its bits to the right.
- The number of iterations is proportional to the number of bits in n, which is O(log n).
- Therefore, the time complexity is O(log n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables such as hammingWeight and carry.
- No additional data structures are used that grow with input size.
- Therefore, the space complexity is O(1).

In summary:
Time complexity: O(log n)
Space complexity: O(1)
"""

"""
Solution 2:

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a counter variable to 0
        count = 0
        # Loop until n is 0
        while n != 0:
            # If the last bit of n is 1, increment the counter
            if n & 1 == 1:
                count += 1
            # Shift n to the right by 1 bit
            n = n >> 1
        # Return the counter
        return count
"""