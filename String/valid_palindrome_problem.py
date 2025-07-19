class ValidPalindrome():
    def isPalindrome(self, s):
        """To check whether string is a palindrome or not"""
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True

vp = ValidPalindrome()
print("is palindrome ? ", vp.isPalindrome(" "))

"""
Time Complexity:
- The algorithm uses two pointers, l and r, which traverse the string from both ends towards the center.
- Each character is visited at most once during the process, either when skipping non-alphanumeric characters or comparing characters.
- Therefore, the overall time complexity is O(n), where n is the length of the input string.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables l, r, and a few temporary variables.
- No additional data structures proportional to the input size are used.
- Hence, the space complexity is O(1).

In summary:
Time complexity: O(n)
Space complexity: O(1)
"""