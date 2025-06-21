class Factorial:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        elif n >= 2:
            return n * self.factorial(n-1)

ft = Factorial()
print("factorial of n ::",ft.factorial(5))