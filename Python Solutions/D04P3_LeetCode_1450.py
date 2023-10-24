class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i,j in zip(startTime,endTime):
            for x in range(i,j+1):
                if x==queryTime:
                    count+=1
        return count
