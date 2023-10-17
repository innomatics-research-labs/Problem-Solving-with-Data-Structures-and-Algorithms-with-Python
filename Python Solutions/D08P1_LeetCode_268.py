#Given an array nums containing n distinct numbers in the range [0, n], 
#return the only number in the range that is missing from the array.
#way_1
class Solution:
  def missingNumber(self, nums: List[int]) -> int:
      real_sum = 0
      missing_sum = 0
      
      for i, num in enumerate(nums): 
          real_sum += i + 1
          missing_sum += num
      
      return real_sum - missing_sum
#Way_2
#Robust way 
#Sum of range [0,n] - sum of given list                #substraction
num_list = list(map(int, input().split(",")))
n = len(num_list)
sum_n = []
for i in num_list:
    sum_n.append(i)
print((n*(n+1)//2)-sum(sum_n))
