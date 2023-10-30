class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num=max(nums)
        for i in range(len(nums)):
            if nums[i]==max_num:
                return i
        
