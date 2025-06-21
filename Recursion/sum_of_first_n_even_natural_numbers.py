class SumEvenNaturalNum:
    def sum_N_even_natural_Num(self, N):
        if N == 1:
            return 2
        else:
            return 2*N + self.sum_N_even_natural_Num(N-1)
             
         
senn = SumEvenNaturalNum()
print("Sum of N Even Natural numbers:: ",senn.sum_N_even_natural_Num(5))