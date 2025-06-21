class SumSquaresNaturalNum:
    def sum_of_squares_N_natural_Num(self, N):
        if N == 1:
            return 1
        else:
            return N**2 + self.sum_of_squares_N_natural_Num(N-1)
             
         
ssnn = SumSquaresNaturalNum()
print("Sum of Sqaures of First N Natural numbers:: ",ssnn.sum_of_squares_N_natural_Num(5))