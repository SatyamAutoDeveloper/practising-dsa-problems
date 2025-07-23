from collections import defaultdict

class DiagonalTraverse:
    def findDiagonalOrder(self, mat):
        diagonal_order = []
        diagonals = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                diagonals[row + col].append(mat[row][col])

        for k in sorted(diagonals.keys()):
            vals = diagonals[k]
            if k % 2 == 0:
                vals = list(reversed(vals))
            diagonal_order.extend(vals)
        return diagonal_order

dt = DiagonalTraverse()
print("Diagonal Traverse Order ::", dt.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))

"""
Time Complexity:
- The nested loops iterate over each element in the matrix exactly once. If the matrix has dimensions m x n, the total number of elements is m * n.
- For each element, appending to the corresponding diagonal list is an O(1) operation.
- Sorting the keys of the diagonals (which are sums of indices) takes O(k log k), where k is the number of diagonals. Since the maximum sum of indices is (m + n - 2), the number of diagonals is at most m + n - 1, so sorting takes O((m + n) log (m + n)).
- Reversing the list for even diagonals is proportional to the length of that diagonal, but across all diagonals, the total reversal cost sums up to O(m * n).

Overall, the dominant term is the traversal of all elements, so the total time complexity is O(m * n + (m + n) log (m + n)).

Space Complexity:
- The 'diagonals' dictionary stores all elements grouped by their diagonal index, requiring O(m * n) space.
- The 'diagonal_order' list stores all elements in the traversal order, also requiring O(m * n) space.

In summary:
Time complexity: O(m * n + (m + n) log (m + n))
Space complexity: O(m * n)
"""