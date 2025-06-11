class SpiralMatrix:
    def spiralOrder(self, matrix):
        """To find the spiral order of the matrix"""
        if not matrix or not matrix[0]:
            print("Spiral Order for given matrix :: []")
            return []
        spiral_order = []
        
        srow = 0
        scol = 0
        erow = len(matrix) - 1
        ecol = len(matrix[0]) - 1

        while srow <= erow and scol <= ecol:
            for i in range(scol, ecol+1):
                """Traverse from left to right"""
                spiral_order.append(matrix[srow][i])
            srow = srow + 1
            
            for j in range(srow, erow + 1):
                """Traverse from top to bottom"""
                spiral_order.append(matrix[j][ecol])
            ecol = ecol - 1
            
            if srow <= erow:
                for i in range(ecol, scol - 1, -1):
                    """Traverse from right to left"""
                    spiral_order.append(matrix[erow][i])
                erow = erow - 1
            
            if scol <= ecol:
                for j in range(erow, srow - 1, -1):
                    """Traverse from bottom to top"""
                    spiral_order.append(matrix[j][scol])
                scol = scol + 1

        return spiral_order

sm = SpiralMatrix()
spiral_order_list = sm.spiralOrder([[2,5],[8,4],[0,-1]])
print("Spiral Order:: ", spiral_order_list)