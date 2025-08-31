class ReverseWords:
    def reverseWords(self, s):
        """To reverse the words of a strings without leading/trailing spaces and single space b/w the two words"""
        s = s.split()
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return " ".join(s)


rw = ReverseWords()
print("String with Reverse Words ::", rw.reverseWords("  hello a  good world  "))

"""
Time Complexity:
- The `split()` operation scans the entire string once, which takes O(n) time, where n is the length of the string.
- Reversing the list of words takes O(k), where k is the number of words, which is at most proportional to n.
- Joining the list back into a string also takes O(n) time, as it processes all characters.
- Overall, the total time complexity is O(n).

Space Complexity:
- The `split()` creates a list of words, which in the worst case can be proportional to n (if the string contains many small words).
- The reversed list and the final string also require additional space proportional to n.
- Therefore, the space complexity is O(n).

In summary:
Time complexity: O(n)
Space complexity: O(n)
"""

"""
Solution 1::

def reverseWords(self, s):
    s = " ".join(s.split()[::-1])
    return s
"""
