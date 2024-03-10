class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = [x for x in nums if x != val]
        k = len(result);
        numEqualTo = len(nums) - k;

        for x in range(numEqualTo): 
             nums.remove(val);
                
        return k;
                
            
        
        