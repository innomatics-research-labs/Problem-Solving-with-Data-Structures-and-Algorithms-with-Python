# Python3 code coming soon
#Way_1
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = 0
        b = 1
        while n:
            k = n % 10
            n //= 10
            a += k
            b *= k
        return b - a

#Way_2 
n = int(input("Enter a integer number i.e. n : "))
prod = 1
sum1 = 0
for digit in str(n) :
    sum1 += int(digit)           #sum1 = sum1 + int(digit)
    prod *= int(digit)           #prod = prod * int(digit)
print("the difference between the product of its digits and the sum of its digits:",prod-sum1)

#Way_3
#way 2
def compute_difference():
    n = int(input())
    sum1 = 0
    prod = 1
    converted_n = str(n)
    for digit in converted_n:
        sum1 += int(digit)           #sum1 = sum1 + int(digit)
        prod *= int(digit)           #prod = prod * int(digit)
    return prod - sum1
#compute_difference()                 #Calling the function
