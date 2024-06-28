class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using Hash table, Time complexity & Space complexity: O(n)
        index_dict = {}
        
        for i in range(len(nums)):
            check = target - nums[i]
            
            if check in index_dict:
                return [i, index_dict[check]]
            else:
                index_dict[nums[i]] = i
            
        #time complexity : O(n^2), Space complexity: O(1)
        #for i in range(len(nums)):
            #for j in range(i+1, len(nums)):
                #if nums[i] + nums[j] == target:
                    #return list([i,j])
                    #return [i,j]
            
                    
            
            