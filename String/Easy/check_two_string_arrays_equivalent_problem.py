class ArrayStringsAreEqual():
    def arrayStringsAreEqual(self, word1, word2):
        """To check if given strings arrays are equal"""
        return "".join(word1) == "".join(word2)

ase = ArrayStringsAreEqual()
print("are two strings arrays equal ?:", ase.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))

"""
Time Complexity:
- Concatenating each array involves traversing all elements and joining their strings.
- Let n be the total number of characters across all strings in word1, and m be the total in word2.
- The join operation takes O(n) for word1 and O(m) for word2.
- The comparison of the two concatenated strings takes O(min(n, m)), but since the strings are of total length n and m, the dominant cost is O(n + m).
- Overall, the time complexity is O(n + m) or O(n)


In summary:
Time complexity: O(n)
Space complexity: O(n)
"""