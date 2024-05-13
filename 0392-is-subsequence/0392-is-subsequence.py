class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        isSub = True
        while i < len(s):
            while j < len(t):
                print(s[i]  + t[j])
                if(s[i] == t[j]):
                    isSub = True
                    break
                else:
                    j += 1
                    isSub = False
                    
            if isSub == True:
                i += 1
                j += 1
                
                if i == len(s):
                    break
                else:
                    isSub = False
            else:
                break
            

        return isSub
                
            
                    
            
                    
                