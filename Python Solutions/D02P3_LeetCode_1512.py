class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        pairs=0
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,val in dic.items():
            if val>=2:
                pairs+=(val*(val-1))//2
        return pairs
