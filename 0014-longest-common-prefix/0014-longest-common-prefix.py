class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        isKeep = False
        i=0
        j=1
        
        while i<len(strs[0]) :
            check = strs[0][i]
            print(check)
            for j in range(len(strs)) :
                if i < len(strs[j]) and check == strs[j][i]:
                    isKeep = True
                else:
                    isKeep = False
                    break
                    
            if isKeep == True:
                common += check
                i+=1
            else :
                break

        return common
        
        
        