"""
Time complexity: O(n * m)
Space complexity: O(m)

This problem can be solved with different approaches like 
1. horizontal scanning
2. vertical scanning
3. Divide and Conquer Algorithm
4. Binary Search
"""
class LongestCommonPrefix():
    def longestCommonPrefix(self, strs):
        lcp_str = []
        idx = 0
        subidx = 0
        if (len(strs) == 1) or (min(strs,key=len) == ""):
            return min(strs,key=len)
        else:
            while len(min(strs,key=len)) > idx:
                lcp_str.append(strs[0][idx])
                for id in range(1, len(strs)):
                    if strs[id][subidx] not in lcp_str[idx]:
                        lcp_str.pop()
                        return "".join(lcp_str)
                    elif strs[id][subidx] in lcp_str[idx]:
                        continue
                subidx += 1
                idx += 1
        return "".join(lcp_str)
            
lcp = LongestCommonPrefix()
print("longest common prefix string is ::", lcp.longestCommonPrefix(["a"])) 

"""
Efficient Solution:

def longestCommonPrefix(self, strs):
        prefix = ""
        minstr = min(strs, key=len)
        for i, letter in enumerate(minstr):
            found = True
            for word in strs:
                if letter != word[i]:
                    found = False
                    break
            if found:
                prefix += letter
            else:
                break

        return prefix
"""