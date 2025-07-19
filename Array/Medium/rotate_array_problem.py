class RotateArray(object):
    def reverse_in_place(self, nums, left, right):
        left = left
        right = right

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums, k):
        """To rotate the k elements with space complexity O(1)"""
        k = k % len(nums)
        self.reverse_in_place(nums, 0, len(nums)-1)
        self.reverse_in_place(nums, 0, k-1)
        self.reverse_in_place(nums, k, len(nums)-1)
        return nums
    
ra = RotateArray()
print("Rotated Array is:: ",ra.rotate([1,2,3,4,5,6,7], 3))

"""
The time complexity of the rotate method is O(n), where n is the length of the input array. This is because the method performs a constant number of reverse operations, each of which traverses the array (or a portion of it) once. Specifically, reversing the entire array takes O(n), reversing the first k elements takes O(k), and reversing the remaining elements takes O(n - k). Since k is at most n, the overall complexity remains O(n).

The space complexity is O(1), meaning it uses a constant amount of extra space. The reversal is done in-place by swapping elements within the input array, and no additional data structures proportional to the input size are used. The only extra variables are for indices and temporary storage during swaps, which do not depend on the size of the input array.
"""