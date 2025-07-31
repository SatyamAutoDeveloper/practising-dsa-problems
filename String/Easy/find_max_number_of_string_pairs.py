class Solution():
    def maximumNumberOfStringPairs(self, words):
        set1 = set()
        maxNumberOfStringPairs = 0
        for word in words:
            pair = word[::-1]
            if pair in set1:
                maxNumberOfStringPairs += 1
            set1.add(word)
        return maxNumberOfStringPairs

sol = Solution()
print(sol.maximumNumberOfStringPairs(["aa","ba","ab"]))


"""
Time Complexity:
- The code iterates through each word in the input list once, which takes O(n) time, where n is the number of words.
- For each word, it performs a string reversal operation (word[::-1]), which takes O(k) time, where k is the length of the word.
- Checking if the reversed string exists in the set is an O(1) average-time operation.
- Adding the current word to the set is also O(1).

Overall, assuming the length of each word is bounded by a constant or small relative to n, the total time complexity is approximately O(n), but if k varies significantly, it becomes O(n * k).

Space Complexity:
- The set `set1` stores up to all the words, so in the worst case, it uses O(n * k) space, where n is the number of words and k is the maximum length of a word.
- Additional variables like `maxNumberOfStringPairs` and `pair` use constant space.

In summary:
- Time complexity: O(n * k), where n is the number of words and k is the maximum length of a word.
- Space complexity: O(n * k).
"""


"""
Solution 1:

def maximumNumberOfStringPairs(self, words):
    maxNumberOfStringPairs = 0
    for idx in range(len(words)):
        if words[idx][::-1] in words[idx+1::]:
            maxNumberOfStringPairs += 1
    return maxNumberOfStringPairs
"""