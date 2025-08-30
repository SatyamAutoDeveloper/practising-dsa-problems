class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        zigzagStr = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                zigzagStr += s[i]
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    zigzagStr += s[i + increment - 2 * r]

        return zigzagStr


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))

"""
Time Complexity:
- The outer loop runs for each row, which is at most numRows times.
- The inner loop iterates over the string with a step size of 'increment' (which is 2 * (numRows - 1)), effectively covering all characters in the string once.
- For each character, the operations are constant time, and at most two characters are appended per iteration.
- Overall, each character in the string is processed a constant number of times, leading to a time complexity of O(n), where n is the length of the input string.

Space Complexity:
- The main additional space is for the output string 'zigzagStr', which in the worst case can be as large as the input string.
- No significant auxiliary data structures are used.
- Therefore, the space complexity is O(n), where n is the length of the input string.

In summary, the algorithm operates in linear time and uses linear space relative to the input size.
"""


"""
Logic Explanation::
===================

The function first checks if numRows is 1. If so, it returns the original string, since a zigzag with one row is just the string itself. Otherwise, it initializes an empty string zigzagStr to build the result.

The outer loop iterates over each row index r. For each row, it calculates an increment, which determines the step size for jumping between characters that belong to the same row in the zigzag pattern. The inner loop starts at the current row index and jumps by increment through the string, appending the appropriate characters to zigzagStr.

For the first and last rows, only one character per cycle is added. For the middle rows, the code checks if there is a "diagonal" character between the vertical columns and adds it if it exists. This is handled by the condition r > 0 and r < numRows - 1 and the calculation i + increment - 2 * r.

Finally, the function returns the constructed zigzag string. The example call demonstrates the conversion for "PAYPALISHIRING" with 4 rows. A subtle point is that string concatenation in Python is not optimal for large inputs; using a list and joining at the end would be more efficient. The logic for calculating the diagonal character index is a common source of confusion, so it's important to understand how the zigzag pattern maps string indices to rows.
"""
