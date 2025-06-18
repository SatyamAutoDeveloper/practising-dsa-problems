"""Time Complexity: O(n^2)"""
class PascalTriangle():
    def pascalTriangle(self, numRows):
        pt_arr = []
        for i in range(numRows):
            if i == 0:
                pt_arr.append([1])
            else:
                prev_row = pt_arr[-1]
                row = [1]
                for j in range(1, i):
                    row.append(prev_row[j - 1] + prev_row[j])
                row.append(1)
                pt_arr.append(row)
        return pt_arr

pt = PascalTriangle()
print("Pascal Triangle ::", pt.pascalTriangle(5))