class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if j!=i and nums[j]<nums[i]:
                    c=c+1
            l.append(c)
        return l

