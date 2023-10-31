class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(partial, left, right, result):
            if len(partial) == 2 * n:
                result.append(partial)
                return
            if left < n:
                generate(partial + '(', left + 1, right, result)
            if right < left:
                generate(partial + ')', left, right + 1, result)

        result = []
        generate('', 0, 0, result)
        return result
