class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


sol = Solution()
print("is Subsequence ?", sol.isSubsequence("abc", "afdbghc"))


"""
Time Complexity:
- The algorithm uses a single while loop that traverses through t once.
- In the worst case, it compares each character of t with characters of s.
- The total number of iterations is proportional to the length of t, which is O(len(t)).
- Since each comparison is constant time, the overall time complexity is O(len(t)).

Space Complexity:
- The algorithm uses only a few variables (i, j) for indexing.
- No additional data structures are used that grow with input size.
- Therefore, the space complexity is O(1).

In summary:
Time complexity: O(len(t))
Space complexity: O(1)
"""
