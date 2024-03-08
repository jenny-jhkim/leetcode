class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numOfOne = s.count("1")
        numOfZero = s.count("0")
        output = ""
        
        if numOfOne == 0:
            output = "0" * len(s)        
        elif numOfOne == 1:
            output = "0"*numOfZero + "1"
        else:
            output = "1"*(numOfOne-1) + "0"*numOfZero + "1"
        
        return output
        
        