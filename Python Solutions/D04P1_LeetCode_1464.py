class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        v1=v2=0
        for num in nums:
            if num>v1:
                v2=v1
                v1=num
            elif num>=v2:
                v2=num
        return ((v1-1)*(v2-1))
