# Python3 code coming soon
#Way_1
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for digit in str(n) :
            s += int(digit)           #s = s + int(digit)
            p *= int(digit)           #p = p * int(digit)
        return (p - s)
