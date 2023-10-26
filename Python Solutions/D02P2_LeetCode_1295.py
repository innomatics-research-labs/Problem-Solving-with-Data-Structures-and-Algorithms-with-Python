# Python3 ,By:- Harsh Udai
# Que. Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        lst=[]
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                lst.append(i)
        return len(lst)

            
            
        
