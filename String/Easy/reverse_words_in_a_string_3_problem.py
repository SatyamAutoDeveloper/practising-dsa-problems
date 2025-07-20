class ReverseWords3():
    def reverseWords(self, s):
        """To reverse the word of strings in-place"""
        s = s.split(" ")
        for idx, ch in enumerate(s):
            s[idx] = ch[::-1]
        return " ".join(s)

rw3 = ReverseWords3()
print("String with reverse words ::", rw3.reverseWords("Let's take LeetCode contest"))

"""
Time Complexity:
- Splitting the string into words takes O(n), where n is the length of the input string.
- Reversing each word with slicing `ch[::-1]` takes O(k) per word, where k is the length of that word. Summed over all words, this is O(n).
- Joining the list back into a string also takes O(n).

Overall, the total time complexity is O(n), since each character is processed a constant number of times.

Space Complexity:
- The split operation creates a list of words, which in the worst case can be proportional to the length of the string, O(n).
- The reversed words are stored in the same list, so no additional significant space is used.
- The final join creates a new string of length proportional to the input, O(n).

Thus, the space complexity is O(n).

In summary:
Time complexity: O(n)
Space complexity: O(n)
"""