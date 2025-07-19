"""I will solve this Later"""
class DiagonalTraverse:
    def findDiagonalOrder(self, mat):
        self.mat = mat
        diagonal_order = []
        for m in range(len(self.mat)):
            for n in range(len(self.mat[m])):
                print("m and n ::",self.mat[m][n])
                

dt = DiagonalTraverse()
dt.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])