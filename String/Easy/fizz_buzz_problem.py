class Solution(object):
    def fizzBuzz(self, n):

        return list(map(
            lambda i: "FizzBuzz" if i % 15 == 0 else
                  "Fizz" if i % 3 == 0 else
                  "Buzz" if i % 5 == 0 else
                  str(i),
            range(1, n + 1)
        ))

sol = Solution()
print("Fizz Buzz :", sol.fizzBuzz(15))


"""
Time Complexity:
- The main operation is a map over the range from 1 to n (inclusive), which has n elements.
- For each element, the lambda function performs a constant number of modulo operations and conditional checks.
- Therefore, the overall time complexity is O(n), as each number is processed exactly once.

Space Complexity:
- The output is a list containing n elements, each being a string ("Fizz", "Buzz", "FizzBuzz", or the number itself as a string).
- The space used to store this list is proportional to n.
- Additional space is used for the lambda function's internal variables, which are constant.
- Hence, the space complexity is O(n).

In summary:
- Time complexity: O(n)
- Space complexity: O(n)
"""


"""
Solution 1:

fb = []
for i in range(1, n+1):
    if i % 15 == 0:
        fb.append("FizzBuzz")
    elif i % 3 == 0:
        fb.append("Fizz")
    elif i % 5 == 0:
        fb.append("Buzz")
    else:
        fb.append(str(i))
return fb

"""