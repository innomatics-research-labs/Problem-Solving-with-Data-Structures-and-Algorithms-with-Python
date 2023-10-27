class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        count[0] = 1
        ans = sum = 0
        for x in nums:
            sum += x
            ans += count[sum-k]
            count[sum] += 1
        return ans  
