class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ['']*len(s)  
        # Initialize an empty string of same length as 's'
        for i in range(len(s)):  
            # Iterate over the string 's'
            output[indices[i]] = s[i]  
            # Assign the character at indices[i] position in 'ans' string
        return ''.join(output)  
        # Convert list of characters to string.
