class AddBinary:
    def addBinary(self, a ,b):
        list1 = []
        len_a = len(a) - 1
        len_b = len(b) - 1
        carry = 0
        while len_a >= 0 or len_b >= 0 or carry:
            total = carry
            if len_a >= 0:
                total += int(a[len_a])
                len_a -= 1    
            if len_b >= 0:
                total += int(b[len_b])
                len_b -= 1
            list1.append(str(total % 2))
            carry = total // 2

        sum_of_binary_num = "".join(list1[::-1])
        return sum_of_binary_num
        
ab = AddBinary()
print("Sum of two binary number ::", ab.addBinary("1", "111"))