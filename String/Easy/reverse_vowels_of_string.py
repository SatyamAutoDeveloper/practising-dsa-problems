class ReverseVowels():
    def reverseVowels(self, s):
        left = 0
        right = len(s)-1
        vowels = 'aeiouAEIOU'
        list1 = list(s)
        while left < right:
            if list1[left] in vowels and list1[right] in vowels:
                list1[left], list1[right] = list1[right], list1[left]
                left += 1
                right -= 1
            elif list1[right] not in vowels:
                right -= 1
            elif list1[left] not in vowels:
                left += 1
                         
        return "".join(list1)

rv = ReverseVowels()
print("String with Reverse Vowels ::",rv.reverseVowels("IceCreAm"))


"""
Time Complexity:
- The main while loop runs until the left index is less than the right index.
- Each iteration potentially moves either the left or right pointer inward.
- In the worst case, each character in the string is examined once, and vowels are swapped when both pointers point to vowels.
- Since each character is processed at most once or twice, the overall time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm converts the input string into a list of characters, which takes O(n) space.
- The list is modified in place, and the final string is reconstructed from this list.
- No additional significant data structures are used that grow with input size.
- Therefore, the space complexity is O(n).

In summary:
- Time complexity: O(n)
- Space complexity: O(n)
"""