"""Time Complexity: O(n^2)"""
class PascalTriangle():
    def pascalTriangle(self, numRows):
        pt_arr = []
        for i in range(numRows):
            if i == 0:
                pt_arr.insert(i, [1])
            elif i == 1:
                pt_arr.insert(i, [1,1])
            else:
                pt_sub_arr = []
                for j in range(len(pt_arr[-1])):
                    if j == 0:
                        pt_sub_arr.append(pt_arr[-1][j])
                    if j < len(pt_arr[-1]) - 1: 
                        pt_sub_arr.append(pt_arr[-1][j] + pt_arr[-1][j+1])
                    else:
                        pt_sub_arr.append(pt_arr[-1][j])

                pt_arr.insert(i, pt_sub_arr)           

        return pt_arr

pt = PascalTriangle()
print("Pascal Triangle ::", pt.pascalTriangle(5))