class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y :
                    if result.count(x) == 0 :
                        result.append(x);
                    break
        return result                  
                