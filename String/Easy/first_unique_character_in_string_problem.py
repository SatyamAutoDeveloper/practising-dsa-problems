class Solution(object):
    def firstUniqChar(self, s):
        dict1 = {}
        for char in s:
            dict1[char] = dict1.get(char, 0) + 1
        
        for idx, char in enumerate(s):
            if dict1[char] == 1:
                return idx

        return -1

sol = Solution()
print("First Unique Char ::", sol.firstUniqChar("loveleetcode"))


"""
Time Complexity:
- The first loop iterates over all characters in the string `s`, which takes O(n) time, where n is the length of `s`.
- The second loop also iterates over all characters in `s`, again O(n).
- The operations inside both loops are constant time (dictionary get/set and comparison).
- Overall, the total time complexity is O(n) + O(n) = O(n).

Space Complexity:
- The dictionary `dict1` stores counts for each unique character in `s`. In the worst case (all characters are unique), it will hold n entries.
- Therefore, the space complexity is O(n).

In summary:
- Time complexity: O(n)
- Space complexity: O(n)
"""


"""
Solution 1:

for idx, char in enumerate(s):
    if char not in s[idx+1:] and char not in s[:idx]:
        return idx
return -1
"""

"""
Solution 2:

left = 0
right = 1
if len(s) >= 2:
    while right <= len(s):
        if s[left] not in s[left+1:] and s[left] not in s[:left]:
            return left
        elif s[right] not in s[right+1:] and s[right] not in s[:right]:
            return right
        left += 2
        right += 2
    return -1
else:
    return 0
"""