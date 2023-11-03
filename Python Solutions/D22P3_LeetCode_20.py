# Python3 code coming soon
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()

        for ch in s:
            if ch in ['[', '{', '(']:
                stack.append(ch)
            elif (len(stack)>0) and ((ch==']' and stack[-1]=='[') or (ch=='}' and stack[-1]=='{') or (ch==')' and stack[-1]=='(')):
                stack.pop()
            else:
                return False
        
        return len(stack)==0
