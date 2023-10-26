class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=[]
        a=0
        for i in range(0,n):
            ans.append(start+i*2)
        for x in ans:
            a=a^x
        return a
