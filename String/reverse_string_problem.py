class ReverseString():
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right]  = s[right], s[left]
            left += 1
            right -= 1
        return s
rs = ReverseString()
print("Reversed Array of string ::",rs.reverseString(["H"]))

"""
The provided code defines a class ReverseString with a method reverseString that reverses a list of characters in place.

Time Complexity:
- The method uses a while loop that runs until the left index is no longer less than the right index.
- In each iteration, it swaps the elements at the left and right indices and then moves the pointers inward.
- Since it processes each element exactly once (swapping pairs from the outer ends towards the center), the total number of iterations is approximately half the length of the list.
- Therefore, the time complexity is O(n), where n is the length of the list.

Space Complexity:
- The reversal is performed in place, requiring no additional data structures proportional to the input size.
- Only a few variables (left, right) are used, which consume constant space.
- Hence, the space complexity is O(1).

In summary:
- Time complexity: O(n)
- Space complexity: O(1)
"""
