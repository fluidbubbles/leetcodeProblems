class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # str_n = str(n)
        # if len(str_n) < 2:
        #     return 0
        # sum_digits = 0
        # prod_digits = 1
        # for i in str_n:
        #     sum_digits += int(i)
        #     prod_digits *= int(i)
        # return prod_digits - sum_digits

        sum_digits, prod_digits = 0, 1
        while n != 0:
            num = n % 10
            sum_digits += num
            prod_digits *= num
            n //= 10
        return prod_digits - sum_digits
