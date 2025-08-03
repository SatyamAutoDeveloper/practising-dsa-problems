class Solution(object):
    def count_of_char(self, s):
        dict1 = {}
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        print(dict1)
        return dict1 
    
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict1= self.count_of_char(s)
        dict2= self.count_of_char(t)
        return dict1 == dict2

sol = Solution()
print("is anagram ?", sol.isAnagram("anagram", "nagaram"))


"""
Time Complexity:
- The count_of_char method iterates through each character in the input string s once, performing constant-time dictionary operations (checking and updating counts). This results in O(n) time, where n is the length of s.
- The isAnagram method calls count_of_char twice (once for s and once for t), each taking O(n) time, and then compares the two dictionaries. Comparing dictionaries in Python takes O(k), where k is the number of unique characters, which is at most the size of the alphabet (constant for fixed character sets). So, the overall time complexity is O(n).

Space Complexity:
- The count_of_char method creates a dictionary to store character counts, which in the worst case (all characters unique) will have size proportional to the length of the string, i.e., O(n).
- The isAnagram method stores two such dictionaries, so total space used is O(n).

In summary:
- Time complexity: O(n)
- Space complexity: O(n)
"""