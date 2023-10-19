class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(n+1):
            ans = ''
            while i > 0:
                rem = i % 2
                ans += str(rem)
                i = i >> 1
            lst.append(ans.count('1'))
        return lst

