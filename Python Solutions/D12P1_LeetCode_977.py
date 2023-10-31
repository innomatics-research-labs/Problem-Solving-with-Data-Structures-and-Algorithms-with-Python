
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ans.append(i*i)
        return sorted(ans)

