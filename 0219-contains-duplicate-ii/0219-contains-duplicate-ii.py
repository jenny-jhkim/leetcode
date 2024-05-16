class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict={}
        min_abs = -1
        for i, num in enumerate(nums):
            if num in num_dict:
                j = num_dict[num] #previous_index
                num_dict[num] = i #update index
                if min_abs == -1 or min_abs > i-j:
                    min_abs = i - j
            else:
                num_dict[num] = i
                
        if min_abs != -1 and min_abs <= k:
            return True
        else:
            return False