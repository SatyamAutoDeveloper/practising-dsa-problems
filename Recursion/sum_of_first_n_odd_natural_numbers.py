class SumOddNaturalNum:
    def sum_N_odd_natural_Num(self, N):
        if N == 1:
            return 1
        else:
            return 2*N-1 + self.sum_N_odd_natural_Num(N-1)
             
         
sonn = SumOddNaturalNum()
print("Sum of N Odd Natural numbers:: ",sonn.sum_N_odd_natural_Num(2))