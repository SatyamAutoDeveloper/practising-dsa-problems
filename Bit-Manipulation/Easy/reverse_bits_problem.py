class Solution(object):
    def reverseBits(self, n):
        bits = []
        decimal_num = 0
        # Convert the n into binary.
        while n > 0:
            bits.append(n % 2)
            n = n >> 1

        # Reverse the binary and Convert the reversed binary nymber into decimal number.
        power = 32 - len(bits)
        for bit in bits[::-1]:
            if bit == 1:
                decimal_num += 1 << power
            power += 1
        return decimal_num


sol = Solution()
print(sol.reverseBits(43261596))

"""
The provided code reverses the bits of a 32-bit integer.

Time Complexity:
- The while loop runs until n becomes zero, which takes at most 32 iterations since n is a 32-bit number.
- The for loop iterates over the bits list, which can have up to 32 elements.
- Overall, both loops combined run in constant time relative to the input size (since the input size is fixed at 32 bits).
- Therefore, the time complexity is O(1).

Space Complexity:
- The bits list stores up to 32 bits, so it uses O(1) space.
- Additional variables (decimal_num, power) use constant space.
- Overall, the space complexity is O(1).

In summary, both time and space complexities are constant, O(1), due to the fixed size of the input (32 bits).
"""
