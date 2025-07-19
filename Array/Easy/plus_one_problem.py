"""Plus One Leet Code Problem"""

class PlusOne:
    def plus_one(self, digits):
        self.digits = digits
        large_integer = ""
        for i in range(len(self.digits)):
            large_integer = large_integer + str(self.digits[i])
        print("large integer ::",large_integer)

        plus_one_large_int = int(large_integer) + 1

        plus_one_large_arr = []
        for i in str(plus_one_large_int):
            plus_one_large_arr.append(int(i))
        return plus_one_large_arr

sol = PlusOne()
plus_one_large_num = sol.plus_one([9])
print("Plus One Large Integer ::", plus_one_large_num)