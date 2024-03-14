class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityNumber = None
        count = 0
                    
        for x in nums:
            if count == 0 :
                majorityNumber = x
                count = 1
            elif x == majorityNumber:
                count+=1
            else :
                count-=1
        
        return majorityNumber
                

                
            