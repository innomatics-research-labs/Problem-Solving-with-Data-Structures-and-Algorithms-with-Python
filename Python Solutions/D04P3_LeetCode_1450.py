class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n=len(startTime)
        cnt=0
        for i in range(n):
            if startTime[i]<=queryTime and endTime[i]>=queryTime:
                cnt+=1
        return cnt
