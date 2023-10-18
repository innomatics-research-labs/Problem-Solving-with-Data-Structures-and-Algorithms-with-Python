#Given an array nums containing n distinct numbers in the range [0, n], 
#return the only number in the range that is missing from the array.
#way_1
class Solution:
  def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)
      sum_n = []
      for i in nums:
        sum_n.append(i)
      return ((n*(n+1)//2)-sum(sum_n))
