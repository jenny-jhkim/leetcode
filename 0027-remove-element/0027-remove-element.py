class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums);
        k = k - nums.count(val);

        while val in nums:
             nums.remove(val)
        return k
                
            
        
        