"""
Time complexity: O(n)
Space complexity: O(n)
"""

from collections import Counter
class EqualByReversingSubarrays():
    def canBeEqual(self, target, arr):
        arr1 = Counter(arr)
        tar1 = Counter(target)
        print(arr1, tar1)
        if arr1 == tar1:
            return True
        return False

eqrevsubarr = EqualByReversingSubarrays()
print("are Arrays equal by reversing sub arrays ::", eqrevsubarr.canBeEqual([809,809,107,274], [809,809,274,107]))
