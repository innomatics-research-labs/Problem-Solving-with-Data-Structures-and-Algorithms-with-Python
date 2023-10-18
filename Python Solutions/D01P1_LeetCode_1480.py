class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        x=0
        for i in nums:
            x = x+i
            result.append(x)
        return result
