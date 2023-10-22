class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr_new=[]

        n=len(nums)//2 
        for i in range(n):
            arr_new.append(nums[i])
            arr_new.append(nums[n+i])
        return arr_new
