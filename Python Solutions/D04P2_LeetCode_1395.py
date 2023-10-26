class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        n=len(rating)
        inc,dec=[0]*(n),[0]*n
        for i in range(n):
            for j in range(i):
                if rating[i]>rating[j]:
                    inc[i]+=1
                    count+=inc[j]
                elif rating[i]<rating[j]:
                    dec[i]+=1
                    count+=dec[j]
        return count
                    
                    
