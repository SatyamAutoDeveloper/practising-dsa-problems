class JewelsInStones(object):
    def numJewelsInStones(self, jewels, stones):
        """To find the count of jewels in stones"""
        total_jewels_in_stones = 0
        for i in range(len(jewels)):
            total_jewels_in_stones += stones.count(jewels[i])
        return total_jewels_in_stones

js = JewelsInStones()
print("No of jewels in stones ::",js.numJewelsInStones("z","ZZ"))

"""
Time Complexity:
- The method iterates over each character in the 'jewels' string, which has length m.
- For each jewel character, it calls stones.count(jewels[i]), which scans through the entire 'stones' string of length n to count occurrences.
- Therefore, for each of the m jewel characters, it performs an O(n) operation.
- Total time complexity is O(m * n).

Space Complexity:
- The method uses a constant amount of extra space: an integer variable total_jewels_in_stones.
- No additional data structures proportional to input size are used.
- Therefore, space complexity is O(1).

In summary:
- Time complexity: O(m * n)
- Space complexity: O(1)
"""