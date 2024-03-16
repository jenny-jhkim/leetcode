class Solution:
    def romanToInt(self, s: str) -> int:
        romanSymbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        i = output = 0
                
        while i < len(s):
            if i + 1 < len(s) and romanSymbols[s[i]] < romanSymbols[s[i+1]]:
            #not last index
                output += romanSymbols[s[i+1]] - romanSymbols[s[i]]
                i += 2
            else :
                output += romanSymbols[s[i]]
                i += 1
            
        return output
        
                    
                
            
            
        