class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)
        length = 0
        
        while i > 0 :
            i -= 1
            if s[i] != ' ':
                length +=1
            elif length > 0:
                return length
            
        return length