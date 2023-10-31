class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low,high=1,x
        while low<=high:
            mid=(low+high)//2
            if mid*mid==x:
                return mid
            elif mid*mid < x:
                low=mid+1
            else:
                high=mid-1
        return high
       
        
