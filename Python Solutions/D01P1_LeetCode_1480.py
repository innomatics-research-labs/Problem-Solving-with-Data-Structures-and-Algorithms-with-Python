class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            running_sum.append(current_sum)
        return running_sum
    

