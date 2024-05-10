class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumString = ""
        result = True
        
        if s.isspace():
            return result
        
        for x in s.lower():
            if x.isalnum():
                alphanumString += x
            
        print(alphanumString)
        
        i = 0
        j = len(alphanumString) - 1

        for i in range(len(alphanumString)):
            if alphanumString[i] != alphanumString[j]:
                result = False
                break
            else: 
                #the caracter is same. go to the next pointer
                j -= 1

        return result