class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numOfOne = s.count("1")
        output = "0" * len(s)        
        output = list(output)
        
        if numOfOne >= 1:   
            for i in range(numOfOne):
                if i == 0:
                    output[len(s)-1] = "1"
                else:
                    output[i-1] = "1"
                    
        output = "".join(output)
        print(numOfOne , output);
        return output
        
        