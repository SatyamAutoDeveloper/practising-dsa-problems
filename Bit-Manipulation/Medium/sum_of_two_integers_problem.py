"""
The value 0xFFFFFFFF is a hexadecimal literal representing a 32-bit mask where all bits are set to 1.

In decimal, 0xFFFFFFFF = 4,294,967,295
In binary, it's 11111111111111111111111111111111 (32 ones).
This is often used in programming to mask or limit values to 32 bits, especially in bitwise operations.

Gotcha:
If you use this mask in a signed 32-bit integer context, it represents -1 due to two's complement representation
"""

class Solution(object):
    def getSum(self, a, b):
        # 32 bits mask in hexadecimal
        mask = 0xFFFFFFFF
        # simulate 32-bit signed integer
        while (b & mask) > 0:
            carry = ((a & b) << 1) 
            a = a ^ b
            b = carry
        # if a is negative in 32-bit signed integer
        if b > 0 :
            return (a & mask)
        else:
            return a


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(1, 1))


# XOR Operation of a and b will have 1 when either a is 0 and b is 1 or b is 0 and a is 1.
# AND operation of a and b will have 1 when a is 1 and b is 1.
# So, we can use XOR operation to add two bits and AND operation to find carry.
# We keep doing this until there is no carry.
# << 1 is used to shift carry to left by 1 bit. like if it is 10 then 100.
# ~ is used to get negative of a number in python.


"""
Time Complexity:
- The loop continues as long as there is a carry (b & mask) > 0.
- In the worst case, each iteration reduces the problem size by resolving one bit of the carry.
- Since integers are represented with 32 bits, the maximum number of iterations is proportional to the number of bits, which is 32.
- Therefore, the time complexity is O(1), as it is bounded by a constant (32 iterations).

Space Complexity:
- The function uses a fixed number of variables (mask, carry, a, b).
- No additional data structures are created that grow with input size.
- Hence, the space complexity is O(1).

In summary, both time and space complexities are constant, O(1), due to the fixed bit-width of 32 bits.
"""