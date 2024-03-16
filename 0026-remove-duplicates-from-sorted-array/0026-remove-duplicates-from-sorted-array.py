class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = k = 1
        currentNumber = nums[0]
        
        while i < len(nums):
            if currentNumber != nums[i] :
                currentNumber = nums[k] = nums[i]
                k+=1
                i+=1
            else:
                #is it last number?
                if currentNumber == nums[-1] : 
                    break
                else :
                    i+=1
        return k;
                
            
            
        