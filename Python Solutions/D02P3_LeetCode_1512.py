class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        total_pairs=0
        for val in d.values():
            val=(val*(val-1))//2
            total_pairs+=val
        return total_pairs
        
