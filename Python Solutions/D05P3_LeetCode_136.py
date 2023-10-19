#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
    
        return result
# XOR of a number with itself gives 0, so all the pairs will cancel each other out The result will be the number that appears only once.
