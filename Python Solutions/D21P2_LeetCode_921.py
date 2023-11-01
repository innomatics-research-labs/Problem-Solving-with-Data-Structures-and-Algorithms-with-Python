class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    count += 1
        return count+len(stack)
