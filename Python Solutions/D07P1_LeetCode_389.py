class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char not in s:
                return char
            else:
                news=s.replace(char,'',1)
                s=news
