class Solution(object):
    def countBits(self, n):
        count_bits = [0]
        for i in range(1, n + 1):
            count_bits.append(count_bits[i >> 1] + i % 2)

        return count_bits


sol = Solution()
print(sol.countBits(5))

"""
The provided code defines a method to compute the number of 1 bits (set bits) in the binary representation of all numbers from 0 up to n.

Time Complexity:
- The loop runs from 1 to n, inclusive, so it executes n times.
- Each iteration performs a constant amount of work: a bitwise right shift, a modulo operation, and list appending.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The list `count_bits` stores n + 1 elements, each representing the count of bits for numbers from 0 to n.
- Hence, the space complexity is O(n).

In summary:
- Time complexity: O(n)
- Space complexity: O(n)
"""



"""
Solution 1:: TC: O(n logn), SC: O(n)

class Solution(object):
    def countBits(self, n):
        count_bits = [0]
        for i in range(1, n + 1):
            carry = 0
            while i > 0:
                carry += i % 2
                i = i >> 1
            count_bits.append(carry)
        return count_bits
"""
