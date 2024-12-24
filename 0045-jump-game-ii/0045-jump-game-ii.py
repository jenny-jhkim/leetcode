class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_counter = 0
        max_reach = 0
        end_of_jump_index = 0

        if len(nums) == 1:
            return jump_counter

        for i in range(len(nums)-1):
                max_reach = max(max_reach, i+nums[i])

                if i == end_of_jump_index:
                    jump_counter +=1
                    end_of_jump_index = max_reach
                
                if end_of_jump_index >= len(nums)-1:
                    break

        return jump_counter

