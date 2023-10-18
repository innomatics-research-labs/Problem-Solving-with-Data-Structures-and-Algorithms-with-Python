# Python3 code coming soon
#Way_1
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum1 = 0
        for digit in str(n) :
            sum1 += int(digit)           #sum1 = sum1 + int(digit)
            prod *= int(digit)           #prod = prod * int(digit)
        return (prod-sum1)
