#(execution time 0ms)
class ReversePrefix():
    def reversePrefix(self, word, ch):
        if ch in word:
            reversed_prefix = ''
            for i in range(len(word)):
                if word[i]==ch:
                    reversed_prefix = reversed_prefix + word[:i+1][::-1]
                    reversed_prefix = reversed_prefix + word[i+1:]
                    break
            return reversed_prefix
        return word

rp = ReversePrefix()
print("Word with reverse prefix ::", rp.reversePrefix("abcdefd", "d"))


"""
Time Complexity:
- The method first checks if ch is in word, which takes O(n) time, where n is the length of word.
- If ch is found, it iterates through the string once (up to the position of ch), which in the worst case is O(n).
- Inside the loop, when ch is found, it performs slicing and reversing operations:
  - word[:i+1][::-1] takes O(i+1) time.
  - Concatenation operations are also O(i+1).
- Overall, the loop runs at most once, and slicing/reversing is proportional to the position of ch.
- Therefore, the total time complexity is O(n) for the search plus O(n) for slicing and concatenation, resulting in O(n) overall.

Space Complexity:
- The method uses additional space for:
  - reversed_prefix string, which in the worst case can be O(n).
  - Temporary strings created during slicing and concatenation.
- Therefore, the space complexity is O(n).

In summary:
Time complexity: O(n)
Space complexity: O(n)
"""


"""
Solution 1:(execution time 1ms)
if ch in word:
    ch_index = word.index(ch)
    return word[:ch_index+1][::-1] + word[ch_index+1:]
return word
"""

"""
Solution 2:(execution time 2ms)
if ch in word:
    ch_index = word.index(ch)
    stack = []
    for idx in range(ch_index+1):
        stack.append(word[idx])
    return "".join(reversed(stack)) + word[ch_index+1:]
return word
"""