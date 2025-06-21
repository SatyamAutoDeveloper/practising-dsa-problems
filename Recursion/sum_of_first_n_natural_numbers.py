class SumNaturalNum:
    def sum_N_natural_Num(self, N):
        if N == 1:
            return 1
        else:
            return N + self.sum_N_natural_Num(N-1)

snn = SumNaturalNum()
print("Sum of N Natural numbers:: ",snn.sum_N_natural_Num(10))