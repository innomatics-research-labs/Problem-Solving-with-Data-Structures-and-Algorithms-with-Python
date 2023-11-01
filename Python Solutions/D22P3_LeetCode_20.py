class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(',']':'[','}':'{'}
        stack = []
        for ch in s:
            if ch in mapping:
                top_el = stack.pop() if stack else '#'
                if top_el != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
