class SpiralMatrix:
    def spiralOrder(self, matrix):
        """To find the spiral order of the matrix"""
        if not matrix or not matrix[0]:
            print("Spiral Order for given matrix :: []")
            return []
        spiral_order = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from Left to Right
            for i in range(left, right + 1):
                spiral_order.append(matrix[top][i])
            top += 1

            # Traverse Downwards
            for i in range(top, bottom + 1):
                spiral_order.append(matrix[bottom if left > right else i][right])
            right -= 1

            if top <= bottom:
                # Traverse from Right to Left
                for i in range(right, left - 1, -1):
                    spiral_order.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse Upwards
                for i in range(bottom, top - 1, -1):
                    spiral_order.append(matrix[i][left])
                left += 1

        print("Spiral Order for given matrix ::", spiral_order)
        return spiral_order


sm = SpiralMatrix()
sm.spiralOrder([[2,5,8],[4,0,-1]])