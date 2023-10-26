class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if nums.count(i)==1:
                ans.append(i)
        return ans
