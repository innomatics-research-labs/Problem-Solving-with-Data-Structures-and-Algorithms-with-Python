# Python3 code coming soon
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            count=0
            for j in range(len(nums)):
                if i>nums[j]:
                    count+=1
            ans.append(count)
        return ans
                
