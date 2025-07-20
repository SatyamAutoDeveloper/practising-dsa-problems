class ReverseDegree(object):
    def reverseDegree(self, s):
        """To find the reverse degree of a string"""
        reverse_alpha_pos = {'a':26, 'b':25, 'c':24, 'd':23, 'e':22, 
                             'f':21, 'g':20, 'h':19, 'i':18, 'j':17,
                             'k':16, 'l':15, 'm':14, 'n':13, 'o':12,
                             'p':11, 'q':10, 'r':9, 's':8, 't':7,
                             'u':6, 'v':5, 'w':4, 'x':3, 'y':2, 
                             'z':1}
        reverse_degree = 0
        for i in range(len(s)):
            reverse_degree += reverse_alpha_pos[s[i]] * (i+1)
        return reverse_degree
rd = ReverseDegree()
print("Reverse Degree ::", rd.reverseDegree("zaza"))

"""
Time Complexity:
- The function iterates through each character in the string s exactly once.
- For each character, it performs a dictionary lookup (which is O(1) on average).
- The total number of operations is proportional to the length of s.
- Therefore, the overall time complexity is O(n), where n is the length of s.

Space Complexity:
- The dictionary reverse_alpha_pos is a fixed size (26 entries), so it consumes constant space, O(1).
- The only additional space used is for variables like reverse_degree and loop counters, which are O(1).
- The input string s is given and not counted as extra space.
- Hence, the space complexity is O(1).

In summary:
Time complexity: O(n)
Space complexity: O(1)
"""