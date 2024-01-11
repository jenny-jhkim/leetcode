class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = 0
        result = digits.copy()
        length = len(digits)
        #convert integer array to integer value
        for i in range(length):
            n = length - 1 - i 
            value += digits[i] * (10**n)      
        #print(value)
        
        if (value + 1) >= (10**length):
            result[0] = 1
            for i in range(1, length):
                result[i] = 0
            result.append(0)
        else :
            value += 1
            
            for i in range(length):
                #print(i, value)
                n = length - 1 - i
                result[i] = value // (10**n) 
                value -= result[i] * (10**n)             
            
        #print(result)
        return result