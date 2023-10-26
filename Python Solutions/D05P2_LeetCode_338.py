class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            count=0
            while i>0:
                r=i%2
                if r==1:
                    count+=1
                i=i>>1
            ans.append(count)
        return ans
