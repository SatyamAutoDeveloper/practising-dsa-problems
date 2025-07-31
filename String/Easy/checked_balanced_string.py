class Solution():
    def isBalanced(self, num):
        odd_sum = 0
        even_sum = 0
        for idx in range(len(num)):
            if idx % 2 == 0:
                even_sum += int(num[idx])
            else:
                odd_sum += int(num[idx])
        if odd_sum == even_sum:
            return True
        return False 
        
sol = Solution()
print(sol.isBalanced("1234"))


"""
The time complexity of the isBalanced method is O(n), where n is the length of the input string num. This is because the method iterates through each character in the string exactly once, performing constant-time operations (integer conversion and addition) during each iteration.

The space complexity is O(1), as the method uses only a fixed amount of additional space regardless of the input size. It maintains a few integer variables (odd_sum and even_sum) and does not allocate any additional data structures that grow with input size.
"""