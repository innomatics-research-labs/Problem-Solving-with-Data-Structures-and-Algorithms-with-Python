class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for key,val in dic.items():
            if val>1:
                return key
