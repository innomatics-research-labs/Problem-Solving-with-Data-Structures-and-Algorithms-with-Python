class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        for i in range(0,len(nums)):
            ans[i]=ans[i-1]+nums[i]
        return ans

