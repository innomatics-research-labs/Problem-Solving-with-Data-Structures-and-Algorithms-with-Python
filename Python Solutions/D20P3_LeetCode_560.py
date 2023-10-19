class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        # N = len(nums)
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                if temp == k:
                    result += 1
        return result
