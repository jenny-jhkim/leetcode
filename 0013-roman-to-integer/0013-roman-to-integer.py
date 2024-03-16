class Solution:
    def romanToInt(self, s: str) -> int:
        romanArray = ["I", "V", "X", "L", "C", "D", "M"]
        intArray = [1, 5, 10, 50, 100, 500, 1000]
        i = j = output = 0
                
        while i < len(s):
            j = romanArray.index(s[i])  
            print(i, j, s[i])
            if i != len(s)-1 and (s[i] == "I" or s[i] == "X" or s[i] == "C"):
                    #not last index
                    nextRoman = s[i+1]        
                    if nextRoman == romanArray[j+1] or nextRoman == romanArray[j+2]:
                        k = romanArray.index(nextRoman)
                        output += intArray[k] - intArray[j]
                        i += 2
                    else:
                        output += intArray[j]
                        i += 1
            else :
                output += intArray[j]
                i += 1
            print(output)
            
        return output
        
                    
                
            
            
        