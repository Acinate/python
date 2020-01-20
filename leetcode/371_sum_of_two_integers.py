class Solution:
    def adder(self, x, y):
        carry = 0
        while y:
            carry = x & y
            x ^= y
            y = carry << 1
        return x

    def subtractor(self, x, y):
        borrow = 0
        while y:
            borrow = (~x) & y
            x ^= y
            y = borrow << 1
        return x

    def getSum(self, a: int, b: int) -> int:
        # Case - 1: Both a and b are positive
        if a >= 0 and b >= 0:
            return self.adder(a, b)
        # Case - 2: Both a and b are negetive
        if a < 0 and b < 0:
            return -self.adder(-a, -b)
        # Case - 3: a is positive and b is negetive
        if a >= 0 and b < 0:
            if -b > a:
                return -self.subtractor(-a, b)
            elif -b < a:
                return self.subtractor(a, -b)
            else:
                return 0
        # Case - 4: a is negetive and b is positive
        if b >= 0 and a < 0:
            if -a > b:
                return -self.subtractor(-a, b)
            elif -a < b:
                return self.subtractor(b, -a)
            else:
                return 0