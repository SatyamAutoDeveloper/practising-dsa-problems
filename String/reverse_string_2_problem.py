class ReverseStr2():
    def reverseStr(self, s, k): 
        left1 = 0
        left2 = k
        slist = []
        while left2 <= len(s):
            slist.append(s[left1:left2][::-1])
            slist.append(s[k+left1:k+left2])
            left1 += 2*k
            left2 += 2*k
        else:
            if len(s) > left1:
                slist.append(s[left1:left2][::-1])
        return "".join(slist)

rs2 = ReverseStr2()
print("Reversed string with 2k chars ::", rs2.reverseStr("abcdefghijklmn", 3))

"""
The provided code defines a method to reverse parts of a string based on the given integer k, processing the string in chunks.

Time Complexity:
- The main while loop iterates over the string in steps of 2*k, so approximately O(n / (2k)) iterations, which simplifies to O(n / k).
- Inside each iteration, slicing operations like s[left1:left2] and s[k+left1:k+left2] are performed, each taking O(k) time because slicing a substring of length k is O(k).
- Reversing the substring with [::-1] also takes O(k) time.
- Therefore, each iteration costs O(k) time, and with about n / k iterations, total time complexity is O((n / k) * k) = O(n).

Space Complexity:
- The list slist stores approximately n / (2k) reversed and unreversed chunks, each of length up to 2k, so total space used is proportional to the size of the output string, which is O(n).
- Additional variables like left1, left2, and temporary substrings use constant space.

Overall:
- Time complexity: O(n)
- Space complexity: O(n)
"""