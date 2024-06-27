class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s={}
        dic_t={}
        
        if len(s) != len(t) :
            return False
        
        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]
            
            if ch_s in dic_s:
                if dic_s[ch_s] != ch_t :
                    return False
                    
            else:
                if ch_t in dic_t:
                    return False
                else:
                    dic_s[ch_s]=ch_t
                    dic_t[ch_t]=ch_s
             
        return True
                
            