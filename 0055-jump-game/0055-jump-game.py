class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+num) #update max reach range
            if max_reach >= len(nums) - 1: #len(nums)-1 means the last index
                return True
        return False

        
        