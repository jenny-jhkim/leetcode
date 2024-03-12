class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = k = 1
        lastNumber = nums[-1]
        currentNumber = nums[0]
        
        while i < len(nums):
            if currentNumber == nums[i] :
                if currentNumber == lastNumber :
                    break
                else:
                    nums.pop(i)  
            else :
                k+=1
                currentNumber = nums[i]
                i+=1
        return k;
                
            
            
        