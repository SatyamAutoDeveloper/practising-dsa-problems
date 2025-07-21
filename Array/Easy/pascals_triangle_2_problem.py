class PascalTriangle2():
    def getRow(self, rowIndex):
        """To get the row of Pascal's Triangle by row index"""
        row = [1]
        for i in range(1, rowIndex + 1):
            # Compute next element using previous element
            row.append(row[-1] * (rowIndex - i + 1) // i)
        return row

pt2 = PascalTriangle2()
print("Row of the given index is ::", pt2.getRow(3))

"""
Time Complexity:
- The method uses a single loop that iterates from 1 up to rowIndex (inclusive).
- Each iteration performs a constant amount of work (multiplication, division, list append).
- Therefore, the overall time complexity is O(rowIndex).

Space Complexity:
- The method creates a list 'row' that stores the elements of the row.
- The size of this list is proportional to rowIndex + 1.
- Hence, the space complexity is O(rowIndex).

In summary:
- Time complexity: O(rowIndex)
- Space complexity: O(rowIndex)
"""