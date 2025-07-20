"""index of the first occurrence of needle in haystack"""
#Time complexity: O(N)
#Space complexity: O(N)

class ImplementStr:
    def strStr(self, haystack, needle):
        idx = 0
        needle_len = len(needle)
        if needle in haystack or (len(needle) <= len(haystack)):
            while idx != len(haystack) - len(needle) + 1:
                if haystack[idx:needle_len] == needle:
                    return idx     
                idx += 1
                needle_len += 1
        return -1

iss = ImplementStr()
print("First occurence of needle at index ::",iss.strStr("abb", "abb"))