class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        
        if len(s) != len(t):
            return False
        
        for ch in s:
            if ch in dict_s:
                dict_s[ch] +=1
            else:
                dict_s[ch] = 1
                
        for ch in t:
            if ch in dict_s:
                dict_s[ch] -= 1
                
                if dict_s[ch] < 0:
                    return False
            else:
                return False
        
        return True